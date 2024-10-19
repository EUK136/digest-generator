import hashlib


print(r"""
 ________  ___  ________  _______   ________  _________        ________  _______   ________   _______   ________  ________  _________  ________  ________     
|\   ___ \|\  \|\   ____\|\  ___ \ |\   ____\|\___   ___\     |\   ____\|\  ___ \ |\   ___  \|\  ___ \ |\   __  \|\   __  \|\___   ___\\   __  \|\   __  \    
\ \  \_|\ \ \  \ \  \___|\ \   __/|\ \  \___|\|___ \  \_|     \ \  \___|\ \   __/|\ \  \\ \  \ \   __/|\ \  \|\  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \   
 \ \  \ \\ \ \  \ \  \  __\ \  \_|/_\ \_____  \   \ \  \       \ \  \  __\ \  \_|/_\ \  \\ \  \ \  \_|/_\ \   _  _\ \   __  \   \ \  \ \ \  \\\  \ \   _  _\  
  \ \  \_\\ \ \  \ \  \|\  \ \  \_|\ \|____|\  \   \ \  \       \ \  \|\  \ \  \_|\ \ \  \\ \  \ \  \_|\ \ \  \\  \\ \  \ \  \   \ \  \ \ \  \\\  \ \  \\  \| 
   \ \_______\ \__\ \_______\ \_______\____\_\  \   \ \__\       \ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\\ \__\ \__\   \ \__\ \ \_______\ \__\\ _\ 
    \|_______|\|__|\|_______|\|_______|\_________\   \|__|        \|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|\|__|\|__|
                                      \|_________|                                                                                                            
""")

print("Let's configure the request information")
#User variables
user = str(input('Set user: '))
realm = str(input('Set realm: '))
password = str(input('Set password: '))
method = str(input('Set request method: '))
url = str(input('Set url: '))
u_nonce = str(input('Set nonce: '))
u_qop = str(input('Set qop: '))
u_nc = str(input('Set nc: '))
u_cnonce = str(input('Set cnonce: '))

#Set info
user_pass = user+':'+realm+':'+password
method_dir = method+':'+'/'+url+'/'
hash1 = hashlib.md5(user.encode('utf8')).hexdigest()
hash2 = hashlib.md5(method_dir.encode('utf8')).hexdigest()
nonce = u_nonce
qop = u_qop
nc = u_nc
cnonce = u_cnonce

#Create hash
string = hash1+':'+nonce+':'+nc+':'+cnonce+':'+qop+':'+hash2
response = hashlib.md5(string.encode('utf8')).hexdigest()

print('The hash is -> '+response)