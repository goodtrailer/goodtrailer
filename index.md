---
layout: base
assets: /assets/index/
carousels:
  - images:
    - image: /assets/index/20220905_142805.jpg
    - image: /assets/index/20220912_172358.jpg
    - image: /assets/index/20220915_171654.jpg
    - image: /assets/index/20230414_225138.jpg
    - image: /assets/index/20230616_161726.jpg
    - image: /assets/index/20230709_102845.jpg
    - image: /assets/index/20230729_191855.jpg
    - image: /assets/index/20230819_145037.jpg
    - image: /assets/index/20230822_155733.jpg
    - image: /assets/index/20230909_113747.jpg
    - image: /assets/index/20230917_142838.jpg
    - image: /assets/index/20231125_124518.jpg
    - image: /assets/index/20240120_033120.jpg
    - image: /assets/index/20240322_185813.jpg
    - image: /assets/index/20240616_083017.jpg
    - image: /assets/index/20240707_120032.jpg
    - image: /assets/index/20240907_085624.jpg
    captions:
    - caption: 9/05/2022
    - caption: 9/12/2022
    - caption: 9/15/2022
    - caption: 4/14/2023
    - caption: 6/16/2023
    - caption: 7/09/2023
    - caption: 7/29/2023
    - caption: 8/19/2023
    - caption: 8/22/2023
    - caption: 9/09/2023
    - caption: 9/17/2023
    - caption: 11/25/202
    - caption: 1/20/2024
    - caption: 3/22/2024
    - caption: 6/16/2024
    - caption: 7/07/2024
    - caption: 9/07/2024
---

{% assign count = page.carousels[0].images.size | minus: 1 %}
{% include carousel.html height="100%" max-height="555px" number="1" first-slide=count %}
