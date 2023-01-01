import numpy as np
sit_ideal=np.array([[90,90,90],[90,90,90],[90,90,90],[90,90,90]])
current_sit=np.array([[110,90,110],[90,90,90],[90,90,90],[90,90,90]])
current_stand=np.array([[130,165,110],[70,165,90],[70,25,90],[110,25,90]])
current_stand_pos_matrix=current_sit-current_stand
ideal_stand_positioin_matrix=sit_ideal-current_stand
error_sit=sit_ideal-current_sit
error_stand=ideal_stand_positioin_matrix-current_stand_pos_matrix
print("GENERAL ERROR MATRIX at SIT POSITION")
print(error_sit)
print("IDEAL STAND POSITION MATRIX TRANSFORMATION")
print(ideal_stand_positioin_matrix)
print("CURRENT STAND POSITION MATRIX TRANSFORMATION")
file=open("FIRMWARE_ALFHA1_0/transformation_matrix.py","w")
file.write("transformation_sit_stand = "+str(current_stand_pos_matrix.tolist()))
file.close()
print(current_stand_pos_matrix)
print("GENERAL ERROR MATRIX at STAND POSITION")
print(error_stand)
