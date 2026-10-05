import warnings
warnings.filterwarnings("ignore")
import pickle as pkl
with open("test_deployment.pkl","rb") as test_machine:
    test_machine = pkl.load(test_machine)
    print(test_machine)
