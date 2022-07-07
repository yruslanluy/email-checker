import poplib

emails = []
i = 0
# pop3server = 'pop.rambler.ru'
# pop3server = poplib.POP3_SSL(pop3server)  # open connection

with open("drafts.txt") as file:
	for line in file:
		# emails.append(line.rsplit(':', 2)[0]+"\n")
		pop3server = 'pop.rambler.ru'
		pop3server = poplib.POP3_SSL(pop3server)  # open connection
		pop3server.user(line.rsplit(':')[0])
		pop3server.pass_(line.rsplit(':')[1])

		pop3info = pop3server.stat()  # access mailbox status
		mail_count = pop3info[0]  # total email
		print(i, line.rsplit(':')[0], ":", mail_count)
		pop3server.quit()
		i += 1

# username = 'pavelsorokinwy3399@rambler.ru'
# password = 'Scottsandra829'

# print(pop3server.getwelcome())  # show welcome message

# pop3info = pop3server.stat()  # access mailbox status
# mail_count = pop3info[0]  # total email
# print("Total no. of Email : ", mail_count)
# print("\n\nStart Reading Messages\n\n")
# for i in range(mail_count):
# 	for message in pop3server.retr(i+1)[1]:
# 		print(message)

# pop3server.quit()


#
# with open("result.txt", "w") as file:
# 	for line in emails:
# 		file.write(line)
