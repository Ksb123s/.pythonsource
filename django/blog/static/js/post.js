document.querySelector("#like").addEventListener("click", (e) => {
  const post_id = e.currentTarget.dataset.post;

  fetch(`/blog/post/like/${post_id}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      document.querySelector(".fs-6 > span").innerHTML = data.like;
      if (data.is_liked) {
        document.querySelector(".like").classList.add("show");
        document.querySelector(".dislike").classList.remove("show");
      } else {
        document.querySelector(".dislike").classList.add("show");
        document.querySelector(".like").classList.remove("show");
      }
    });
});
