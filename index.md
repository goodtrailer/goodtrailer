---
layout: base
assets: /assets/index/
---

<script>
    const pool = [
        ["{{page.assets}}20220905_142805.jpg", "9/05/2022"],
        ["{{page.assets}}20220912_172358.jpg", "9/12/2022"],
        ["{{page.assets}}20220915_171654.jpg", "9/15/2022"],
        ["{{page.assets}}20230414_225138.jpg", "4/14/2023"],
        ["{{page.assets}}20230616_161726.jpg", "6/16/2023"],
        ["{{page.assets}}20230709_102845.jpg", "7/09/2023"],
        ["{{page.assets}}20230729_191855.jpg", "7/29/2023"],
        ["{{page.assets}}20230819_145037.jpg", "8/19/2023"],
        ["{{page.assets}}20230822_155733.jpg", "8/22/2023"],
        ["{{page.assets}}20230909_113747.jpg", "9/09/2023"],
        ["{{page.assets}}20230917_142838.jpg", "9/17/2023"],
        ["{{page.assets}}20231125_124518.jpg", "11/25/2023"],
        ["{{page.assets}}20240120_033120.jpg", "1/20/2024"],
        ["{{page.assets}}20240322_185813.jpg", "3/22/2024"],
        ["{{page.assets}}20240616_083017.jpg", "6/16/2024"],
        ["{{page.assets}}20240707_120032.jpg", "7/07/2024"],
        ["{{page.assets}}20240907_085624.jpg", "9/07/2024"]
    ];

    const featured = pool.length - 1;
    const useFeatured = true;

    let choice = pool[featured];
    if (Math.random() < 0.5 || !useFeatured)
    {
        const r = Math.floor(Math.random() * (pool.length - 1));
        choice = pool[r >= featured ? r + 1 : r];
    }

    window.addEventListener("load", (e) => {
        document.getElementById("featured-pic").setAttribute("src", choice[0]);
        document.getElementById("featured-desc").textContent = choice[1];
    });
</script>

![](){:.figure #featured-pic style="max-height: 555px"}
*/ /*{:#featured-desc}
