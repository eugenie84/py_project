# write a program that will display the account id from the arn
# set up a variable arn
arn = "arn:aws:clouddirectory:us-west-2:12345678910:schema/published/cognito/1.0"

# split a variable arn by colon (:)
arn_split = arn.split(":")
print (arn_split)

# Extract the account id
account_id = arn_split[4]

# print the account id
print ("The aws account id is:\t", account_id)
