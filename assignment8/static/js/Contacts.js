console.log("shinuy")


fetch("https://reqres.in/api/users?page=2").then(response=>response.json())
.then(responseJSON => CreateUserList(responseJSON.data)).catch(err => console.log(err));


function CreateUserList(users){
    const Main= document.querySelector("main");
        for(let user of users){
            console.log(users)
            const section = document.createElement("section");
            section.innerHTML= `
            <div>
                <img src="${user.avatar}" alt="User Avatar">
                <p> ${user.first_name} ${user.last_name}</p>
                <p> ${user.email}</p>
            </div>
            `;
            Main.appendChild(section)
        }
}