# Introduction
The problem of predicting if a DNA sequence contains or not a promoter region is an important problem in bioinformatics, mainly because determining the promoter region in the DNA is a significant step in the process of detecting gens. As the conditions for 
a DNA sequence to function as a promoter are not known, machine learning and deeplearning models are still developed to approach the problem of promoter identification in the DNA. In this project, we are proposing a deep learning MLP model for solving 
the considered problem.

# Objective
The purpose of this project is to develop a system for classifying DNA promotor genes to determine if they are affected by a common bacteria, Escherichia coli(E.coli) and will be used for taking precautions from these microbes and will be able to fed into another 
high level DNA driven problems.

# Key Components
• The project aims to develop a system for classifying DNA promoter genes to determine if they are affected by E.coli infection.
• The system includes a deep learning MLP (Multi-Layer Perceptron) model for  promoter gene classification.
• A Django web application will be created to provide a user-friendly interface for inputting DNA sequences and obtaining classification results.

# Dataset 
• This dataset has been developed to help evaluate a hybrid learning algorithm, KBNN.
• The dataset contains a total of 106 records, divided into 2 classes. The records are evenly distributed, with 53 records assigned to class ‘+’ (representing promoter genes) and 53 records assigned to class ‘-’ 
(representing non-promoter genes)
• Include 3 attributes:
1. One of {+/-}, indicating the class ("+" = promoter).
2. The instance name (non-promoters named by position in the 1500-long nucleotide sequence provided by T. Record).
3. 3-59. The remaining 57 fields are the sequence, starting at position -50 (p-50) and ending at position +7 (p7). Each of these fields is filled by one of {a, g, t, c}.

# Deep Learning MLP Model Design:
• Input Data: This is the input data representing DNA sequence, typically composed of sequence of nucleotides (A, T, C, G).
• Pre-processing: Pre-processing steps may include One-hot encoding, which converts each nucleotide into a vector representation. Checking for and handling any missing or incomplete sequences.
• Input Layer: Represents the input layer of the neural network. It consists of 228 nodes (57*4)
• Hidden layers: These layers perform feature extraction and capture complex patterns in the input sequences. Multiple hidden layers allow the model to learn hierarchical representations.
• Output Layer: The output layer provides the final prediction. In this binary classification task, a sigmoid activation function is typically used to output probabilities indicating whether the DNA is promoter or not.
• Classification Result: this is the final output of the model, indicating whether the input DNA is promoter or not.
• Training Process: 
Optimizer: Adam
Loss function: Binary cross-entropy
• Model Evaluation: Evaluation metrics used to assess the performance of the MLP model
Accuracy

# Django Web Application Design: 
 • Frontend: 
Home Page: Contains a form to input DNA sequences. Provide a default sample DNA sequence for users who are unfamiliar with input format.
Result Page: Displays the classification result.
Database View Page: Shows all input DNA sequences stored in the database.
Design using HTML and CSS.
• Backend: 
Django Framework: Utilize Django for handling HTTP requests, routing
and views.
Views: Implement views for rendering HTML templates and processing 
user inputs.
Models: Define a model to store DNA sequences in the database.
Forms: Create a form for user input validation.
