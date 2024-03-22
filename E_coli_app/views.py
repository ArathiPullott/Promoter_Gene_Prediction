# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from django.shortcuts import redirect
from tensorflow import keras
from .forms import DNASequenceForm
from .models import DNASequence
import tensorflow as tf
from django.utils.html import format_html

def home_page(request):
    return render(request, 'index.html')

def input_sequence(request):
    if request.method == 'POST':
        form = DNASequenceForm(request.POST)
        if form.is_valid():
            sequence = form.cleaned_data['sequence']
            data = pd.DataFrame({'Sequence': sequence}, index=[range(0,1)])
            # reshaped_sequence = np.array(sequence).reshape(1, -1)
            split_data = data['Sequence'].str.split('', expand=True)
            # Drop columns 0 and 58
            split_data.drop(columns=[0,58], inplace=True)
            # Rename columns from 0 to 57
            new_column_names = [str(i) for i in range(0, 57)]
            split_data.columns = new_column_names

            one_hot_encoder = pickle.load(open('final_encoder.pkl', 'rb'))
            promoter_model = pickle.load(open('final_Model.pkl', 'rb')) 
            encoded_sequence = one_hot_encoder.transform(split_data)
            # Make predictions using the loaded model

            prediction = promoter_model.predict(encoded_sequence)
            affected_by_ecoli = prediction > 0.5  # Example threshold for binary classification
            sequence = form.save(commit=False)
            sequence.affected_by_ecoli = affected_by_ecoli
            sequence.save()
            # Perform any processing or analysis you need here
            return redirect('result')
    else:
        form = DNASequenceForm()
    return render(request, 'input.html', {'form': form})
# def result(request, pk):
#     sequence = DNASequence.objects.get(pk=pk)
#     return render(request, 'result.html', {'sequence': sequence})
def result(request):
    # Retrieve the current DNA sequence from the database
    current_sequence = DNASequence.objects.first()
    return render(request, 'result.html', {'current_sequence': current_sequence})

def previous_results(request):
    # Retrieve all DNA sequences from the database
    all_sequences = DNASequence.objects.all()

    # Create lists to store data
    sequences_data = []
    results = []
    creation_dates = []

    # Extract data from each sequence
    for sequence in all_sequences:
        sequences_data.append(sequence.sequence)
        results.append(sequence.affected_by_ecoli)
        creation_dates.append(sequence.created_at)

    # Create a DataFrame
    df = pd.DataFrame({
        'Sequence': sequences_data,
        'Affected_by_E_coli': results,
        'Creation_Date': creation_dates
    })
    result_html = df.to_html(index=False)

    return render(request, 'previous_results.html',{'result_html': format_html(result_html)})
