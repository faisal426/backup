


// for(let gpt=30;gpt>=3;gpt-=3){
//   console.log('forloop: '+gpt)
// }
// 
for(let b=1;b<=5;b+=1){
  console.log('forloop: '+b)
}

let a= 1
while(a<=5){
  console.log('while: ' +a)
  a+=1
}

let c= 10
do{
  console.log('dowhile:'+c)
  c+=1
}while(c<=8)
// 

let array= ['apel','mangga','jeruk']

for(let forof of array){
  console.log(forof)
}

let object= {nama: 'faisal',umur: '89',kelas: 3}

for(let forin in object ){
  console.log(forin + ': '+object[forin])
}