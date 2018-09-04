import urllib.request as url
import re
import urllib


#findall returns element in the list format
text=url.urlopen("http://tuiost.edu.np").read().decode('utf-8')
hello=re.findall('B.Sc. CSIT (.*?) Semester Exam result',text)
result=("".join(hello))
data="B.Sc. CSIT "+result+" Semester Exam result"
print(data)


def roman_to_int(roman):
    """Convert from Roman numerals to an integer."""
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 
              'X': 10, 'V': 5, 'I': 1}
    numbers = [values[char] for char in roman]
    total = 0
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1
    res1=(total + num2)
    link="http://tuiost.edu.np/pdf/bs"+str(res1)+".pdf"
    data=url.urlretrieve(link,result)
    print("\n download is goingS on")

    for i in range(1,100):
    	print("*\t-----*------\t *------\t-----*")

    if data:
    	print("file has been successfully downloaded")
    
    


    
roman_to_int(result)    
