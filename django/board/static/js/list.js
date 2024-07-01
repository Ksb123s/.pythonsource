const actionForm = document.querySelector("#actionForm");
// 제목 클릭시 actionform 보내기
document.querySelector("tbody").addEventListener("click", (e) => {
  e.preventDefault();
  // alert(e.target.href);
  href = e.target.href;
  if (href != undefined) {
    actionForm.action = href;
    actionForm.submit();
  }
});

// 정렬 변화가 일어나면
document.querySelector(".form-select").addEventListener("change", (e) => {
  // alert(e.target.value);
  actionForm.querySelector("#so").value = e.target.value;
  actionForm.submit();
});

// 페이지 나누기 + 검색어
// 페이지 나누기 클릭시 href 에 있는 값 가져오기
//  actionform의 page value 변경하기

document.querySelectorAll(".page-item").forEach((i) => {
  i.addEventListener("click", (e) => {
    e.preventDefault();
    page = e.target.getAttribute("href");
    actionForm.querySelector("#page").value = page;
    actionForm.submit();
  });
});

// 검색어(top_keyword) 가져오기
// 없는 경우 alert()

// 있는 경우
// actionForm keyword value에 삽입
//            page value 1로 변경

document.querySelector("#btn_search").addEventListener("click", () => {
  const top_keyword = document.querySelector("#top_keyword");

  if (top_keyword.value === "") {
    alert("검색어를 입력해 주세요");
    top_keyword.focus();
    return;
  }

  actionForm.querySelector("#keyword").value = top_keyword.value;
  actionForm.querySelector("#page").value = 1;
  actionForm.submit();
});
