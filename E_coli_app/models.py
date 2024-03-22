from django.db import models

# Create your models here.
class DNASequence(models.Model):
    sequence = models.CharField(max_length=100)  # Assuming DNA sequences are less than 100 nucleotides
    affected_by_ecoli = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.sequence