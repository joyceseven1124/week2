function avg(data){
// 請用你的程式補完這個函式的區塊
   let total = 0;
   let member = 0;
   let dataEM =[];
   for (let key in data["employees"]){
        dataEM = data["employees"][key];
        if(dataEM["manager"] == false ){
            total = total + dataEM["salary"];
            member ++;
        }
    }
    console.log(total/member);
}
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":false
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":true
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":false
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":false
        }
    ]
}); // 呼叫 avg 函式