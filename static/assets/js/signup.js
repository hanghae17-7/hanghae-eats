const password = document.getElementById("password");
const passwordConfirm = document.getElementById("password_confirm");
const passwordMessage = document.getElementById("password_message");
const errormsg = document.getElementById("error-msg");
const signup = document.getElementById("signup");

function passwordChecker(e) {
  e.preventDefault();
  password.addEventListener("input", function () {
    const passwordValue = password.value;

    // 비밀번호의 최소 자릿수를 정의 (예: 8자)
    const minPasswordLength = 8;
    // 특수 문자 포함 여부를 확인하는 정규 표현식
    const specialCharRegex = /[!@#$%^&*()]/;
    console.log(passwordValue);
    // 비밀번호 자릿수 및 특수 문자 검증
    if (passwordValue.length < minPasswordLength) {
      passwordMessage.innerHTML =
        "비밀번호는 최소 " + minPasswordLength + "자여야 합니다.";
      password.setCustomValidity(
        "비밀번호는 최소 " + minPasswordLength + "자여야 합니다."
      );
    } else if (!specialCharRegex.test(passwordValue)) {
      passwordMessage.innerHTML =
        "비밀번호에 !@#$%^&*() 중 하나 이상의 특수 문자를 포함해야 합니다.";
      password.setCustomValidity(
        "비밀번호에 !@#$%^&*() 중 하나 이상의 특수 문자를 포함해야 합니다."
      );
    } else {
      passwordMessage.innerHTML = "";
      password.setCustomValidity("");
    }
  });

  passwordConfirm.addEventListener("input", function () {
    if (password.value !== passwordConfirm.value) {
      passwordConfirm.setCustomValidity("비밀번호가 일치하지 않습니다.");
      passwordMessage.innerHTML = "비밀번호가 일치하지 않습니다.";
    } else {
      passwordConfirm.setCustomValidity("");
      passwordMessage.innerHTML = "";
    }
  });
}

function trySignUp(e) {
  e.preventDefault();
  console.log(password.value);
  console.log(passwordConfirm.value);

  if (password.value != passwordConfirm.value) {
    alert("비밀번호가 일치하지 않습니다!");
  } else {
    const formData = new FormData();
    formData.append("username", document.getElementById("username").value);
    formData.append("nickname", document.getElementById("nickname").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("password", document.getElementById("password").value);

    console.log(formData);

    fetch("/signup", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        if (data.result == "success") {
          alert("회원가입이 완료되었습니다.");
          window.location.replace("/login");
        } else {
          console.log(data.error);
          errormsg.textContext = data.error;
        }
      })
      .catch((r) => {
        window.location.replace("/signup");
        console.log("catch에 걸림");
      });
  }
}
function init() {
  document.addEventListener("DOMContentLoaded", passwordChecker, false);
  signup.addEventListener("submit", trySignUp, false);
}

init();
