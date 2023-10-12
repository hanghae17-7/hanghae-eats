const loginForm = document.getElementById("login-form");
const errormsg = document.getElementById("error-msg");
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
        window.location.replace("/myaccount"); // 로그인 성공했으므로 가게리스트 페이지로 이동
      } else {
        errormsg.textContent = "비밀번호가 틀렸습니다.";
      }
    })
    .catch((r) => {
      window.location.replace("/login");
      console.log("catch에 걸림");
    });
}

function init() {
  loginForm.addEventListener("submit", loginformsubmit, false);
}

init();
