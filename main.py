def permu4(number):

        number = 'x' + number

        result = ''
        temp = []
        temp = [2, 4, 3, 1]
        for i in temp:
            result += number[i]
        return result

def permu8(number):

        number = 'x' + number

        result = ''
        temp = []
        temp = [6, 3, 7, 4, 8, 5, 10, 9]
        for i in temp:
            result += number[i]
        return result

def permu10(number):

        number = 'x' + number

        result = ''
        temp = []
        temp = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        for i in temp:
            result += number[i]
        return result

def cut(number):
        return number[0: int(len(number)/2)], number[int(len(number)/2)
        
        :  len(number)]

def shift_left( bit, left_number, right_number):
        for i in range(bit):
            left_result = left_number[1: len(left_number)] + left_number[0]
            left_number = left_result

        for i in range(bit):
            right_result = right_number[1: len(right_number)] + right_number[0]
            right_number = right_result
        return left_result, right_result

def inper( bit, number):
        number = 'x' + number
        result = ''
        temp = []
        if bit == 8:
            temp = [2, 6, 3, 1, 4, 8, 5, 7]

        for i in temp:
            result += number[i]

        return result

def inper_inverse( bit, number):
        number = 'x' + number
        result = ''
        temp = []
        if bit == 8:
            temp = [4, 1, 3, 5, 7, 2, 8, 6]

        for i in temp:
            result += number[i]

        return result

def ep( bit, number):
        number = 'x' + number
        result = ''
        expand = [4, 1, 2, 3, 2, 3, 4, 1]
        for i in expand:
            result += number[i]
        return result

def xor( key, number):
        result = ''
        for i in range(len(number)):
            if number[i] == key[i]:
                result += '0'
            else:
                result += '1'
        return result

def sbox( numl, numr):
        s0 = [['01', '00', '11', '10'], ['11', '10', '01', '00'],
              ['00', '10', '01', '11'], ['11', '01', '11', '10'], ]

        s1 = [['00', '01', '10', '11'], ['10', '00', '01', '11'],
              ['11', '00', '01', '00'], ['10', '01', '00', '11'], ]

        rl = int(numl[0] + numl[3], 2)
        cl = int(numl[1] + numl[2], 2)

        rr = int(numr[0] + numr[3], 2)
        cr = int(numr[1] + numr[2], 2)

        return s0[rl][cl] + s1[rr][cr]

def sw( num):
        return cut(num)[1] + cut(num)[0]

def gen_key( key):
        k = permu10(key)
        lh, rh = cut(k)
        lh, rh = shift_left(1, lh, rh)
        k1 = permu8(lh + rh)

        lh, rh = shift_left(2, lh, rh)
        k2 = permu8(lh + rh)

        return k1, k2

def encrypt( key, plain):
        enc = execute_encrypt(key ,plain)
        return enc
       

def decrypt( key, cipher):
        des = execute_decrypt(key,cipher)
        return des


def execute_encrypt(key ,plain):
        k1, k2 = gen_key(key)

        p = inper(8, plain)
        lh, rh = cut(p)
        op = ep(4, rh)
        op = xor(k1, op)
        sr = sbox(cut(op)[0], cut(op)[1])
        op = permu4(sr)
        op = xor(lh, op)
        op = op + rh

        op = sw(op)

        lh, rh = cut(op)
        op = ep(4, rh)
        op = xor(k2, op)
        sr = sbox(cut(op)[0], cut(op)[1])
        op = permu4(sr)
        op = xor(lh, op)
        op = op + rh
        cipher = inper_inverse(8, op)
        return cipher
    
           
def execute_decrypt(key,cipher):
        k1, k2 = gen_key(key)
        p = inper(8, cipher)
        lh, rh = cut(p)
        op = ep(4, rh)
        op = xor(k2, op)
        sr = sbox(cut(op)[0], cut(op)[1])
        op = permu4(sr)
        op = xor(lh, op)
        op = op + rh

        op = sw(op)

        lh, rh = cut(op)
        op = ep(4, rh)
        op = xor(k1, op)
        sr = sbox(cut(op)[0], cut(op)[1])
        op = permu4(sr)
        op = xor(lh, op)
        op = op + rh
        plain = inper_inverse(8, op)
        return plain
def ctop():

    ciphers =  ['0b10011101','0b1110011','0b11001101','0b1100011','0b11000','0b11001101','0b1100011','0b10011101','0b10011101','0b11000','0b11000','0b1100011','0b11000011','0b1001000','0b110','0b110','0b110','0b10011101','0b11001101','0b110','0b11010011','0b110','0b11000011','0b10010110','0b10010110','0b11000','0b1100011','0b11000011','0b1001000','0b11000011','0b1100011','0b10010110','0b1110011','0b10010110','0b11000','0b11000','0b1110011','0b11001101','0b1100011','0b11010011','0b10011101','0b10010110','0b11010011','0b10011101','0b11000','0b1110011','0b1100011','0b10010110','0b11000','0b10010110','0b110','0b10010110','0b10011101','0b1001000','0b11000','0b10010110','0b110','0b11000011','0b10011101','0b1110011','0b10011101','0b11001101','0b110','0b10010110','0b10010110','0b1100011','0b11000011','0b11001101','0b11000','0b1110011','0b11000011','0b11000011','0b10011101','0b1001000','0b1110011','0b10010110','0b11001101' ]
    student_number = '590610655'

    c_key = 0


  
    for i in range(1024):
        key = str(bin(i))[2:]
        key = key.zfill(10)

        cipher_list = []
        count_correct_cipher = 0

     
        for num in range(10):

            plain = bin(ord(str(num)))[2:]
            plain = plain.zfill(8)

            cipher = encrypt(key=key, plain= plain)
            cipher_list.append(cipher)

        for index,number in enumerate(student_number):
            if(cipher_list[int(number)] == ciphers[index][2:].zfill(8)):
                count_correct_cipher += 1
            else: 
                break
   
        if(count_correct_cipher >= 9):
            c_key = str(bin(i))[2:].zfill(10)
            print('\n\nKey :', c_key)


    print('\nPlain text : ')
    for cipher in ciphers:
        cipher = str(cipher[2:].zfill(8))
        plain = decrypt(key = c_key, cipher = cipher)
        #plain = chr(int(plain,2))
        
        print (plain)

ctop()
