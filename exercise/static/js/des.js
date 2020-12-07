let ip_matrix = [58,50,42,34,26,18,10,2,
                                    60,52,44,36,28,20,12,4,
                                    62,54,46,38,30,22,14,6,
                                    64,56,48,40,32,24,16,8,
                                    57,49,41,33,25,17,9,1,
                                    59,51,43,35,27,19,11,3,
                                    61,53,45,37,29,21,13,5,
                                    63,55,47,39,31,23,15,7];

let ip_reverse_matrix = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
                                                       38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
                                                       36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
                                                       34,2,42,10,50,18,58, 26,33,1,41, 9,49,17,57,25];

let  key_to56_matrix = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,
                                        10, 2,59,51,43,35,27,19,11,3,60,52,44,36,
                                        63, 55,47,39,31,23,15,7,62,54,46,38,30,22,
                                        14,6,61,53,45,37,29,21,13,5,28,20,12,4];

let key_shift_matrix = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1];
let key_shift_sum_matrix = [1,2,4,6,8,10,12,14,15,17,19,21,23,25,27,28];

let key_to48_matrix = [14,17,11,24,1,5,
                                                    3,28,15,6,21,10,
                                                    23,19,12,4,26,8,
                                                    16,7,27,20,13,2,
                                                    41,52,31,37,47,55,
                                                    30,40,51,45,33,48,
                                                    44,49,39,56,34,53,
                                                    46,42,50,36,29,32];

let r0_to48_matrix = [32,1,2,3,4,5,
                                                4,5,6,7,8,9,
                                                8,9,10,11,12,13,
                                               12,13,14,15,16,17,
                                               16,17,18,19,20,21,
                                               20,21,22,23,24,25,
                                               24,25,26,27,28,29,
                                               28,29,30,31,32,1];

let pbox_matrix = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
                                            2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25];

let s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
                    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
                    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
                 [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]] ;

let s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
                    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
                    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
                 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]];

let s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
                  [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
                  [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
                    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]];

let s4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
               [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
               [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
                 [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]];

let s5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
               [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
                  [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
               [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]];

let s6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
                 [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
                   [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
                   [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]];

let s7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
                [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
                  [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
                  [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]];

let s8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
                    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
                    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
                    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]];

let str_plain = "1001100110011001100110011001100110011001100110011001100110011001";
let str_cipher = "0101010101010101010101010101010101010101010101010101010101010101";

function split_str_encode(str,num)
{
    let strArr = [];
    let len = str.length ;
    for( let i = 0 ; i < len/num ; i++)
    {
        let strslice = str.slice(num*i,num*(i+1));
        strArr.push(strslice);
    }
    let anslen = strArr.length ;
    let lastlen = strArr[anslen-1].length ;
    let lennum = 56-lastlen;
    let makeupnum = 0 ;
    if(lastlen <= 56) {
        while(lennum>0) {
            strArr[anslen-1] = strArr[anslen-1] + "0";
            lennum--;
            makeupnum++;
        }
        strArr[anslen-1] = strArr[anslen-1] + str_makeup(dec2binstr(makeupnum),8,0);
    }
    else{
        let makenum = 64 - lastlen+56;
        strArr[anslen-1] = str_makeup(strArr[anslen-1],64,1);
        let tmpstr = str_makeup(dec2binstr(makenum),64,0);
        strArr.push(tmpstr);
    }
    return strArr ;
}

function split_str_decode(str,num)
{
    let strArr = [];
    let len = str.length ;
    for( let i = 0 ; i < len/num ; i++)
    {
        let strslice = str.slice(num*i,num*(i+1));
        strArr.push(strslice);
    }
    let anslen = strArr.length ;
    while(strArr[anslen-1].length != num){
        strArr[anslen-1] = strArr[anslen-1] + "0" ;
    }
    return strArr ;
}

function str_makeup(str,len,func)
{
    let slen = str.length ;
    if(slen >= len)
        return str ;
    else if(func == 0) {
        while(str.length < len)
            str = "0" + str ;
    } else {
        while(str.length < len)
            str = str + "0"  ;
    }
    return str ;
}

function upload(input) {
    //支持chrome IE10
        let file = input.files[0];
        let filename = file.name.split(".")[0];
        let reader = new FileReader();
        reader.readAsText(file);
        reader.onload = function() {
            let str = this.result ;
            str =str.replace(/(\s|\n|\t|\v|\f|\r)*/g,"");
            document.getElementById("plaintext").value= str;
        }
        document.getElementById("ciphertext").value = "";
        document.getElementById("inf").innerText = "";
}


function download(filename, text) {
    let element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function getans()
{
    let str = document.getElementById("ciphertext").value ;
    if(str.length == 0){
        alert("please upload the file first and then encode or decode")
    } else {
        download("ans.txt",str);
    }
}

function str_convert(str,cmatrix) // change an array according to the given matrix and return str
{
    let clength = cmatrix.length ;
    let ansArr = new Array(clength);
    for( let i = 0 ; i < clength ; i++){
        ansArr[i] = str[cmatrix[i]-1];
    }
    return ansArr.join("");
}

function looprshift(str,num)
{
    let slen = str.length ;
    num = num % slen ;
    return str.substring(slen-num,slen) + str.substring(0,slen-num)  ;
}
function looplshift(str,num)
{
    let slen = str.length ;
    num = num % slen ;
    return  str.substring(num,slen) + str.substring(0,num) ;
}

function binstr2dec(str)
{
    let slen = str.length ;
    let ans = 0 ;
    for(let i = 0 ; i < slen ; i++){
        ans += Number(str[slen-1-i])*Math.pow(2,i);
    }
    return ans ;
}

function get_xor(str1,str2)
{
    let len = str1.length ;
    let ansArr = new Array(len);
    for(let i = 0 ; i < len ; i++){
        if(str1[i] == str2[i])
            ansArr[i] = "0";
        else
            ansArr[i] = "1";
    }
    return ansArr.join("");
}

function dec2binstr(num)
{
    return num.toString(2);
}

function get_numins(str,sArr) // not test str.length = 6
{
    let rowstr = str[0]+str[5];
    let colstr = str.substring(1,5);
    let row = binstr2dec(rowstr);
    let col = binstr2dec(colstr);
    let ans = dec2binstr(sArr[row][col]) ;
    while(ans.length < 4){
        ans = "0"+ans ;
    }
    return ans ;
}

function sbox_convert(str) //str.length = 48
{
    let str1 = str.substring(0,6) ;
    let str2 = str.substring(6,12) ;
    let str3 = str.substring(12,18) ;
    let str4 = str.substring(18,24) ;
    let str5 = str.substring(24,30) ;
    let str6 = str.substring(30,36) ;
    let str7 = str.substring(36,42) ;
    let str8 = str.substring(42,48) ;

    let ans1 = get_numins(str1,s1);
    let ans2 = get_numins(str2,s2);
    let ans3 = get_numins(str3,s3);
    let ans4 = get_numins(str4,s4);
    let ans5 = get_numins(str5,s5);
    let ans6 = get_numins(str6,s6);
    let ans7 = get_numins(str7,s7);
    let ans8 = get_numins(str8,s8);

    return ans1+ans2+ans3+ans4+ans5+ans6+ans7+ans8;
}

function key_shift(str,num)
{
    let str_a = str.substring(0,28);
    let str_b = str.substring(28,56);
    let str_a_aftershift = looplshift(str_a,key_shift_sum_matrix[num-1]) ;
    let str_b_aftershift = looplshift(str_b,key_shift_sum_matrix[num-1]) ;
    return str_a_aftershift + str_b_aftershift
}

function get_key(str,num) // This is the function to get the key of every round, str is the cipher and the num is the times of round
{
    let str_afterchosen = str_convert(str,key_to56_matrix); // 64 to 56
    let str_aftershift = key_shift(str_afterchosen,num); // split to 2 part and do the operation of left shift, them join to get the 56 str, num stands for  the round x
    return str_convert(str_aftershift ,key_to48_matrix);//them 56 to 48
}

function round_des(plaintext,cipher,num,func) // num stands for the times of des
{
        let key ;
        if(func == 0)
            key = get_key(cipher,num) ;
        else
            key = get_key(cipher,9-num) ;
        let l0 = plaintext.substring(0,32) ;
        let r0 = plaintext.substring(32,64) ;
        let r0_afterextend = str_convert(r0,r0_to48_matrix);
        let after_xor = get_xor(r0_afterextend,key) ;
        let after_sbox = sbox_convert(after_xor); // length = 32
        let after_pbox = str_convert(after_sbox,pbox_matrix);
        let final_r1 = get_xor(l0,after_pbox);
        let final_l1 = r0 ;
        let ans ;
        if(num != 8)
            ans = final_l1 + final_r1;
        else
            ans =  final_r1 + final_l1 ;
        return ans ;

}

// round_des(str_plain,str_cipher,1) ;

function des(plaintext,cipher,func) // func = 0 encode, func = 1 decode // des for 64 bit
{
    let plaintext_after_ip = str_convert(plaintext,ip_matrix);
    let str = plaintext_after_ip ;
    for(let i = 1 ; i <= 8 ; i++) {
        let str_after_round = round_des(str,cipher,i,func) ;
        str = str_after_round ;
    }
    return str_convert(str,ip_reverse_matrix);
}

function all_des_encode(plaintext,cipher) // des for more bits
{
    let strArr = split_str_encode(plaintext,64) ; // plaintex
    let ansArr = [];    // ciphertext
    let len = strArr.length ;
    let initial_vector = document.getElementById("iv").value; // can be any vector whose len is 64.
    let tmpstr ;
    for(let i = 0 ; i < len ; i++) {
        if(i == 0){
            tmpstr = get_xor(strArr[i],initial_vector) ;
        } else {
            tmpstr = get_xor(strArr[i],ansArr[i-1]) ;
        }
        ansArr.push(des(tmpstr,cipher,0)) ;
    }
    return ansArr.join("") ;
}
//1111111100000000111111110000000011111111000000001111111100000000
function all_des_decode(plaintext,cipher) // des for more bits
{
    let strArr = split_str_decode(plaintext,64) ; // plaintex
    let len = strArr.length ;
    let ansArr = new Array(len);    // ciphertext
    let initial_vector = document.getElementById("iv").value ; // can be any vector whose len is 64.
    let tmpstr ;
    for(let i = len-1 ; i >= 0 ; i--){
        tmpstr = des(strArr[i],cipher,1);
        if( i == 0){
            tmpstr = get_xor(tmpstr,initial_vector) ;
        } else {
            tmpstr = get_xor(tmpstr,strArr[i-1]) ;
        }
        ansArr[i] = tmpstr ;
    }
    return ansArr.join("") ;
}

function encode()
{
    let cipher = document.getElementById("cipher").value
    let plaintext = document.getElementById("plaintext").value;
    let initial_vector = document.getElementById("iv").value;
    if(cipher.length != 64 || initial_vector.length != 64){
        alert("cipher/initial vector not 64 bits");
        return ;
    }
    if(cipher.length != 64)
        cipher = str_makeup(cipher,64,0);
    let ciphertext = all_des_encode(plaintext,cipher) ;
    document.getElementById("ciphertext").value= ciphertext ;
    if(plaintext.length != 0)
        document.getElementById("inf").innerText = "Encoding successfully!";
}

function decode()
{
    let cipher = document.getElementById("cipher").value ;
    let plaintext = document.getElementById("plaintext").value;
    let initial_vector = document.getElementById("iv").value;
    if(cipher.length != 64 || initial_vector.length != 64){
        alert("cipher/initial vector not 64 bits");
        return ;
    }
    if(cipher.length != 64)
        cipher = str_makeup(cipher,64,0);
    let ciphertext = all_des_decode(plaintext,cipher) ;
    let cipherlen = ciphertext.length;
    let makeupnum = binstr2dec(ciphertext.substring(cipherlen-8,cipherlen));
    let finalciphertext = ciphertext.substring(0,cipherlen-8-makeupnum);
    document.getElementById("ciphertext").value = finalciphertext ;
    if(plaintext.length != 0)
        document.getElementById("inf").innerText = "Decoding successfully!";
}