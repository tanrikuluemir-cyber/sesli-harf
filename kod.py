sesli_harf="aeıioöuüAEIİOÖUÜ"
kelime=input("bir kelime giriniz")

count=0
for i in kelime:
    if i in sesli_harf:
        count+=1

        
print("sesli harf sayısı:",count)
