from django.shortcuts import render
from dossiers.models import societes
# Create your views here.



# Example usage
def Show_dossiers():
    # Query all societes objects
    all_societes = societes.objects.all()
    
    # Print the raisonSocial of each societe
    for societe in all_societes:
        print(societe.raisonSocial)
