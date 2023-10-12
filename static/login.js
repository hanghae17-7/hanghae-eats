const loginForm = document.getElementById("login-form");

function loginformsubmit(e) {
  e.preventDefault();

  const formData = new FormData();
  formData.append("email", document.getElementById("email").value);
  formData.append("password", document.getElementById("password").value);

  console.log(formData);

  fetch("/login", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data.result == "success") {
        document.cookie = "mytoken=" + data.token + "; path=/";
        window.location.replace("/storelist"); // 로그인 성공했으므로 가게리스트 페이지로 이동
      } else {
        console.log("로그인 fail data 넘어옴");
      }
    })
    .catch((r) => {
      console.log("서버에서 토큰 데이터가 넘어오지 않는 예외");
    });
}

// axios
//   .post("/login", data)
//   .then(function (response) {
//     if (response["data"]["result"] == "success") {
//       document.cookie =
//         "mytoken=" + response["data"]["result"]["token"] + "; path=/";
//       window.location.replace("/login/token-check");
//     } else {
//       console.log("response undefined");
//     }
//   })
//   .catch(function (error) {
//     console.log(error);
//   });

function init() {
  loginForm.addEventListener("submit", loginformsubmit, false);
}

init();
