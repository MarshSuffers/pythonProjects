#Define Variables, lists, and such

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

post_message = []

#Define Functions
def is_message_acceptable():
    for i in message:
        if i not in alphabet:
            return False

def is_shift_acceptable():
    if shiftInt > 26 or shiftInt < -26 or shiftInt == 0:
        return False

def shift_message():
    for i in message:
        myIndex = alphabet.index(i)
        myShift = myIndex + shiftInt
        post_message.append(alphabet[myShift])

#Main Program

print("This a a caeser cipher decoder/encoder!")

message = input("Write your message with no spacing or special characters: ")
message.lower()
message = list(message)

if is_message_acceptable() == False:
    print("Next time, write your message with no spacing or special characters.")
    quit()

shift = input("How big do you want your shift to be? ")
try:
    int(shift)
except ValueError:
    print("Write an *integer* next time.")
    quit()

shiftInt = int(shift)

if is_shift_acceptable() == False:
    print("Next time, please input a number between -26 and 26 that is NOT 0.")
    quit()

shift_message()

print("".join(post_message))
