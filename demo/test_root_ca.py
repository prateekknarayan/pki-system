from ca.root_ca import RootCA

ca = RootCA()

result = ca.create_root_ca("MyRootCA", "strongpassword")

print("Root CA created:")
print(result)
