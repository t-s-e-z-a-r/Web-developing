import requests
g = 'https://newton.vercel.app/api/v2/simplify/'
x = str(input("Введіть вираз: "))
st =[]
for i in x:
    st.append(i)
x =""
for i in  range(len(st)):
    if st[i] == "+":
        st.remove(st[i])
        st.insert(i, "%2B")
    if st[i] == "/":
        st.remove(st[i])
        st.insert(i, "%2F")
    x+=st[i]
print(x)
ht = g + x
res = requests.get(ht)
print(res.json())
