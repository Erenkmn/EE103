""" def sum_odd_digits(number):
    total = 0
    while True :
        temp= number%10
        if temp%2 == 1 :
            total += temp
        if number < 10:
            break
        number //= 10
        
    return(total)


def repeat_with_seperator(text,n):
    ntext = text
    for i in range(1,n):

        ntext = "-".join([ntext,text])
    return(ntext)


def get_last_info(text):
    temp=""
    i=0
    while True:
        if text[i] == IndexError:
            break
        temp = text(i)
        i+=1   
    if i == 0 :
        tupy = ("",-1)
    else:
        tupy = (temp,i)

    return(tupy)

get_last_info("eren")
 """



""" 
def reverse_text(text):
    ntext=""
    for i in text:
        ntext = i + ntext
    return(ntext)



def sum_string_digits(text):
    temp = 0
    for i in text:
        if i.isdigit() == True:
            temp +=int(i)
    return(temp)


def draw_stairs(word, n):
    stair = ""
    for i in range(n):
        stair += word 
        if i != n-1 :
            stair += "\n"
    return(stair)
 """



def is_palindrome_recursive(text):
    text.lower()
    if text[n] == text[-n]:



    
        










