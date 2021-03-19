m=input("Enter the plain text or the original message:- ")
k=int(input("\nEnter the key:- "))
print("\nThe Cipher text or the Secret message is:-",end=' ')
while True:
    for i in range(len(m)):
        if m.isalpha():
            i=ord(m[i])+k
            print(chr(i),end='')
        else:
            print(" Invalid message bits")
            n=input("Re-enter the plain text or the original message:- ")
            print("The Cipher text or the Secret message is:-",end=' ')
            for j in range(len(n)):
                if n.isalpha():
                    j=ord(n[j])+k
                    print(chr(j),end='')
    break
