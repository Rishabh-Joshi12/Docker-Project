
import os
choice=0
print("\t\t\t\t  TUI ")
print("\t\t\t ---------------------")
print("\t\t\t\tWELCOME ")
print("\t\t\t ---------------------")
while choice!=6:
	print("\t\t\t\n\n SELECT YOUR CHOICE")
	print("\t 1. Start Docker Services")
	print("\t 2. Check Available Images")
	print("\t 3. Pull a image from docker hub")
	print("\t 4. Run docker conpose for setting the environment for wordpress ")
	print("\t 5. Launch docker container for hosting website. ")
	print("\t 6. Get public ip for your website hosted on apache server")
	print("\t 7. Stop docker services")
	print("\t 8. EXIT\n")
	choice=input("\t ENTER YOUR CHOICE: ")
	choice=int(choice)
	if(choice==1):
		os.system("systemctl start docker")
		print("\t !!Docker service is started!!")
	elif(choice==2):
		print("\t Available images in your system are:")
		print(os.system("docker images"))

	elif(choice==3):
		imag=input("\t Enter image name")
		print(os.system("docker pull {}".format(imag)))
	elif(choice==4):
		os.system("cd Desktop/docker-project")
		print(os.system("docker-compose up"))
	elif(choice==5):
		print("\t Pulling httpd from docker hub")
		print(os.system("docker pull httpd:2.4"))
		print(os.system("sudo docker run -dit --name httpd-server -p 8080:80 -v /home/user/website/:/usr/local/apache2/htdocs/ httpd:2.4"))
		print("\t Copy your files in /home/user/website/ ")
		print(os.system("\t Hey! Your server is configured"))
	elif(choice==6):
		print("Installing NGROX")		
		os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
		os.system("cd Downloads")
		os.system("unzip ngrok-stable-linux-amd64.zip")
		os.system("cd ngrok-stable-linux-amd64")
		os.system("./ngrok http 80")	
	elif(choice==7):
		print("\t !!Docker service is stopped!!")
		print(os.system("systemctl stop docker"))
	elif(choice==8):
		break
	else:
		print("INVALID CHOICE")





