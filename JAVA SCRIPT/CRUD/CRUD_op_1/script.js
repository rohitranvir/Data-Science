let displayDatacontainer=document.body.querySelector(".displaydata")
let getTask=async ()=>{
    let res=await fetch ("http://localhost:3000/tasks")
    let data=await res.json()
    data.forEach(element => {
        let taskContainer=document.createElement("article")
        let name=document.createElement("p")
        let description=document.createElement("p")
        let editbtn=document.createElement("button")
        let delbtn=document.createElement("button")
        let btncontainer=document.createElement("aside")
        name.innerText=element.title
        description.innerText=element.task
        editbtn.innerText="EDIT"
        delbtn.innerText="DELETE"
        delbtn.addEventListener("click",()=>{
            deleteTask(element.id)
        })
        btncontainer.append(editbtn,delbtn)
        taskContainer.append(btncontainer,name,description)
        displayDatacontainer.append(taskContainer)
    });
}
getTask()
let form =document.querySelector("form")
form.addEventListener("submit",(e)=>{
    e.preventDefault()
    let formdata=new FormData(form)
    console.log(formdata.get("name"));
    console.log(formdata.get("description"));   
    let details={
        title:formdata.get("name"),
        task:formdata.get("description")
    } 
    addTask(details)
})
let addTask=async(details)=>{
    await fetch("http://localhost:3000/tasks",{
        method:"POST",
        headers:{
            "content-type":"application/json"
        },
        body:JSON.stringify(details)
    })
}
deleteTask=async(id)=>{
await fetch(`http://localhost:3000/tasks/${id}`,{
    method:"DELETE"
})
}