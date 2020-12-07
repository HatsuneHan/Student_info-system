// let a = BigInt("999999999999999");
// let b = BigInt("999999999999888");
//
// let d = (a*b).toString(2);
// let e = a*b
// let c = BigInt("0b"+ d);
function randomBetween(max, min = 0n) {
    max = BigInt(max);
    min = BigInt(min);
    if (max < min) {
        [max, min] = [min, max]
    }
    const range = max - min;
    const count = calculatePrecision(range);
    let random = new Array(Number(count))
        .fill(0)
        .map(() => BigInt(Math.floor(Math.random() * (2 ** 32))))
        .map((int, index) => int << (BigInt(index) * 32n))
        .reduce((acc, int) => acc + int, 0n);


    let bitCount = countBits(range);
    let minRandom = random >> ((32n * count) - bitCount);
    if (minRandom > range) return randomBetween(max, min);
    else return minRandom + min;
}
function calculatePrecision(range) {
    const result = range >> 32n;
    if (result >= 1n) {
        return calculatePrecision(result) + 1n;
    }
    return 1n;
}
function countBits(range) {
    const result = range >> 1n;
    if (result >= 1n) {
        return countBits(result) + 1n;
    }
    return 1n;
}

function ext_gcd_getreverse(n,e){
    if (n < e){
        return false;
    }
    let pren = n ;
    let r = n % e, q = n / e;
    let s0 = 1n, s1 = 0n, t0 = 0n, t1 = 1n;
    while(r != 0n){
        let s2 = s0 - q*s1, t2 = t0 - q*t1;
        s0 = s1; s1 = s2;
        t0 = t1; t1 = t2;
        n = e;
        e = r;
        r = n % e;
        q = n / e;
        // alert(t1);
    }
    let rev = t1;
    if(rev < 0n)
        rev += pren ;
    return rev;
}

function calpow(a,m,n) // a^m % n
{
    let b = 1n;
    a = a % n ;
    while(m != 0n){
        if(m & 1n)
            b = (b*a) % n;
        m >>= 1n;
        a = (a*a) % n ;
    }
    return BigInt(b) ;
}

// document.write(calpow(2n,6n,30n));

function Miller_Rabin(numstr)
{
    let n = BigInt(numstr) ;
    if((!(n & 1n)) && n != 2n)
        return false;
    let k = 0 ;
    let nmone = n-1n ;
    let m = nmone;
    while( !(m & 1n)) {
        k++;
        m >>= 1n;
    }
    // document.write(k.toString()+"     "+nmone.toString())
    let a = randomBetween(nmone,1n);
    // document.write(a.toString() + "</br>");
    let b = calpow(a,m,n);
    // document.write("finish");
    if(b == 1n)
        return true;
    else{
        for(let i = 0 ; i <= k-1 ; i++) {
            if( b == n - 1n)
                return true;
            else {
                b = (b**2n) % n;
            }
        }
    }
    return false ;
}

function get_random(num)
{
    let strArr = [];
    for(let i = 0 ; i < num ; i++){
        let ran = Math.floor(Math.random() * 2);
        if(i != 0)
            strArr.push(ran);
        else
            strArr.push("1");
    }
   return strArr.join("");
}

function get_prime(num)
{
    let n = BigInt("0b"+ get_random(num)) ;
    // document.write(n);
    while(!Miller_Rabin(n)){
        n = BigInt("0b"+ get_random(num));
    }
    // document.write(n);
    return n;
}

function get_mul_prime_str()
{
    let a = get_prime(64) ;
    let b = get_prime(64);
    while(b == a)
        b = get_prime(64);
    let n = a*b ;
    n = n.toString(2) ;
    return [a,b,n] ;
}

function  get_mul_prime()
{
    let tmp = get_mul_prime_str();
    let ans = tmp[2];
    while(ans.length != 128){
        tmp = get_mul_prime_str()
        ans = tmp[2];
    }
    return [tmp[0],tmp[1],tmp[0]*tmp[1]];
}

function euler(a,b)
{
    return (a-1n)*(b-1n);
}

function getdl(num,bitnum)
{
    let dl = get_prime(bitnum-1);
    while(num % dl == 0n || dl >= num){
        dl = get_prime(bitnum-1);
    }
    return dl;
}

function getel(dl,eulernum)
{
    return ext_gcd_getreverse(eulernum,dl);
}

function rsa_getkey()
{
    let n = get_mul_prime();
    let dl = getdl(euler(n[0],n[1]),128);
    let el = getel(dl,euler(n[0],n[1]));
    // alert(el*dl % euler(n[0],n[1]));
    return [n[2],dl,el];
}

function rsa_encode(plaintext,el,nl) // plaintext is 01 str
{
    let  num = calpow(BigInt("0b"+plaintext),el,nl);
    return num.toString(2);
}

function rsa_decode(ciphertext,dl,nl,len=0)
{
    let ansstr = calpow(BigInt("0b"+ciphertext),dl,nl).toString(2);
    if(len > ansstr.length) {
        let makeupnum = len - ansstr.length;
        while(makeupnum--)
            ansstr = "0"+ansstr ;
    }
    return ansstr;
}

function rsa_encode_display() // plaintext is 01 str
{
    let plaintext = document.getElementById("rsaplaintext").value;
    let strel = document.getElementById("rsael").value;
    let strnl = document.getElementById("rsanl").value;
    let el = BigInt(document.getElementById("rsael").value);
    let nl = BigInt(document.getElementById("rsanl").value);

    let  num = calpow(BigInt("0b"+plaintext),el,nl);


    if(plaintext.length != 0 && strel.length !=0  && strnl.length != 0){
        document.getElementById("afterrsa").value = num.toString(2);
        document.getElementById("infen").innerText = "Encoding successfully!";
    }
}

function rsa_decode_display(len)
{
    let ciphertext = document.getElementById("rsaciphertext").value;
    let dl = BigInt(document.getElementById("dersadl").value);
    let nl = BigInt(document.getElementById("dersanl").value);

    let strdl = document.getElementById("dersadl").value ;
    let strnl = document.getElementById("dersanl").value;

    let ansstr = calpow(BigInt("0b"+ciphertext),dl,nl).toString(2);
    if(len > ansstr.length) {
        let makeupnum = len - ansstr.length;
        while(makeupnum--)
            ansstr = "0"+ansstr ;
    }
    if(ciphertext.length != 0 && strdl.length != 0 && strnl.length != 0)
    {
        document.getElementById("deafterrsa").value = ansstr ;
        document.getElementById("infde").innerText = "Decoding successfully!";
    }


}

function get_cipher()
{
    let key = rsa_getkey();
    let nl = key[0];
    let dl = key[1];
    let el = key[2];
    let outputn = document.getElementById("outputn");
    let outputd = document.getElementById("outputd");
    let outpute = document.getElementById("outpute");

    outputn.value = nl ;
    outputd.value = dl ;
    outpute.value = el;

}

// let key = rsa_getkey();
// let plaintext = "00011111010101100";
// let nl = key[0];
// let dl = key[1];
// let el = key[2];
// document.write(plaintext);
// document.write("</br>");
// let ciphertext = rsa_encode(plaintext,el,nl);
// document.write(ciphertext);
// document.write("</br>");
// let revplaintext  = rsa_decode(ciphertext,dl,nl,17);
// document.write(revplaintext);

