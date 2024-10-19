import hashlib


banner = r"""
________  .__                        __      ________                                   __                
\______ \ |__| ____   ____   _______/  |_   /  _____/  ____   ____   ________________ _/  |_  ___________ 
 |    |  \|  |/ ___\_/ __ \ /  ___/\   __\ /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \\
 |    |   \  / /_/  >  ___/ \___ \  |  |   \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
/_______  /__\___  / \___  >____  > |__|    \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
        \/  /_____/      \/     \/                 \/     \/     \/     \/           \/                   
"""

print(banner)
print("Let's configure the request information...")
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