# this is the code to rename root files coming out of the Geant4 simulation
# please remember, this will work only if the root files are ordered according to the follwoing momenta list:
# 0.1, 0.2, 0.5, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 3.0, 3.5, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0, 18.0, 21.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100.0
# If Geant4 did not produce one or two files because the corresponding momenta are below the Cherenkov threshold, this will still work.

### this is the dictionary that maps root file names with the corresponding momenta values
momentumDictionary = {}

def main():



if __name__=="__main__":
    ### call the main function above
    main()

