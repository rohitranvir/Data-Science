let displayDataContainer=document.querySelector(".displaydata");
let gettaskdata=async ()=>{
    let res=await fetch("http://localhost:3000/tasks")
    let data =await res.json();
    data.forEach(element => {
        let taskContainer=document.createElement("article");
        let title=document.createElement("p");
        let description=document.createElement("p");
        let editbtn=document.createElement("button");
        let delbtn=document.createElement("button");
        let btncontainer=document.createElement("aside");
        // ! Assigning values to element
        title.innerText=element.title ;
        description.innerText=element.task;
        editbtn.innerText="Edit";
        delbtn.innerText="Delete";
        //! Assigning the function
        editbtn.addEventListener("click",()=>{
            updatedata(element)
        })
        delbtn.addEventListener("click",()=>{
            deleteTask(element.id)
        })
        //! Append The children
        btncontainer.append(editbtn,delbtn);
        taskContainer.append(title,description,btncontainer);
        displayDataContainer.append(taskContainer)


    });    
};
gettaskdata()
// ! Accessing the form from HTML
let form =document.querySelector("form")
form.addEventListener("submit",(e)=>{
e.preventDefault()
let formData=new FormData(form)
// console.log(formData.get("name"));
// console.log(formData.get("description"));
let details={
    title:formData.get("name"),
    task:formData.get("description")
}
addTask(details)
})
 
// ! Create  the task
let addTask=async(data)=>{
    await fetch("http://localhost:3000/tasks",{
        method:"post",
        headers:{
            "content-type":"application/json"
        },
        body: JSON.stringify(data),
    })
} 

//! Deleting task
let deleteTask=async(id)=>{
    await fetch(`http://localhost:3000/tasks/${id}`,{
        method:"DELETE",
    })

}

let updatedata=async(element)=>{
    let task=document.getElementsByName("name")
    let description=document.getElementsByName("description")
    console.log(task);
    console.log(description);
    task[0].value=element.title;
    description[0].value=element.task;
}
