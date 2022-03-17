# opening files for reading
with open("reference.txt") as f:
    f1 = f.read()

with open("hypothesis.txt") as f:
    f2 = f.read()
    
f1 = f1.split()
f2 = f2.split()

# list of common words
common_words_list = ["the", "of", "and", "a", "be", "this", "there", "an", "been", "some"]

# removing words from the given files
file1_data = [x for x in f1 if x not in common_words_list]
file2_data = [x for x in f2 if x not in common_words_list]

lev_matrix = []
# Nested loops to initialize matrix
for i in range(len(file2_data) + 1):
    rows = [i]
    for j in range(len(file1_data)):
        if i == 0:
            rows.append(j + 1)
        else:
            rows.append(0)
    lev_matrix.append(rows)

for i in range(1, len(file2_data) + 1):
    for j in range(1, len(file1_data) + 1):

        # Check if both strings are same
        if file1_data[j - 1] == file2_data[i - 1]:
            lev_matrix[i][j] = lev_matrix[i - 1][j - 1]
        else:
            lev_matrix[i][j] = min(lev_matrix[i - 1][j], lev_matrix[i][j - 1], lev_matrix[i - 1][j - 1]) + 1

# initializing variables
i = len(lev_matrix[0]) - 1
j = len(lev_matrix) - 1
substitution = 0
deletion = 0
insertion = 0

while (True):
    # if the matrix ends, break the loop
    if i == 0 or j == 0:
        break

    # if deletion occurs
    if lev_matrix[j][i] == lev_matrix[j][i - 1] + 1:
        if file1_data[i - 1] not in common_words_list:
            deletion += 1
        i = i - 1
    # if both alphabets are same, go to the next diagonal position
    elif file1_data[i - 1] == file2_data[j - 1]:
        i = i - 1
        j = j - 1
    # if substitution occurs
    elif lev_matrix[j][i] == lev_matrix[j - 1][i - 1] + 1:
        if file1_data[i-1] not in common_words_list :
            if file2_data[j-1] not in common_words_list:
                substitution += 1
        i = i - 1
        j = j - 1
    # if insertion occurs
    elif lev_matrix[j][i] == lev_matrix[j - 1][i] + 1:
        if file1_data[i - 1] not in common_words_list :
            insertion += 1
        j = j - 1


lev_distance = substitution + deletion + insertion
res = "\nLevenstein Distance is: " + str(lev_distance)
res += "\nSubstitutions : " + str(substitution)
res += "\nDeletions : " + str(deletion)
res += "\nInsertions : " + str(insertion)

with open("result_task3.txt", 'w', encoding='utf8') as f:
    f.write(res)

print("\nLevenstein Distance is: ", lev_distance)

print("\nSubstitutions : ", substitution)
print("Deletions : ", deletion)
print("Insertions : ", insertion)
