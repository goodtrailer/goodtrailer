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
    - image: /assets/index/20240928_191339.jpg
    - image: /assets/index/20241003_102528.jpg
    - image: /assets/index/20241101_225522.jpg
    - image: /assets/index/20241105_220025.jpg
    - image: /assets/index/20241111_104352.jpg
    - image: /assets/index/20241203_161504.jpg
    - image: /assets/index/20241226_152038.jpg
    captions:
    - caption: 9/05/2022, 2:28pm
    - caption: 9/12/2022, 5:23pm
    - caption: 9/15/2022, 5:16pm 
    - caption: 4/14/2023, 10:51pm &mdash; kamiya's blue whale
    - caption: 6/16/2023, 4:17pm
    - caption: 7/09/2023, 10:28am
    - caption: 7/29/2023, 7:18pm
    - caption: 8/19/2023, 2:50pm
    - caption: 8/22/2023, 3:57pm
    - caption: 9/09/2023, 11:37am
    - caption: 9/17/2023, 2:28pm 
    - caption: 11/25/2023, 12:45pm
    - caption: 1/20/2024, 3:31am &mdash; kamiya's little bird
    - caption: 3/22/2024, 6:58pm
    - caption: 6/16/2024, 8:30am
    - caption: 7/07/2024, 12:00pm
    - caption: 9/07/2024, 8:56am
    - caption: 9/28/2024, 7:13pm
    - caption: 10/03/2024, 10:25am &mdash; kamiya's pegasus
    - caption: 11/01/2024, 10:55pm
    - caption: 11/05/2024, 10:00pm &mdash; bioluminescence
    - caption: 11/11/2024, 10:43am
    - caption: 12/03/2024, 4:15pm &mdash; hojyo's violinist
    - caption: 12/26/2024, 3:20pm
---

{% assign count = page.carousels[0].images.size | minus: 1 %}
{% include carousel.html height="100%" max-height="555px" number="1" first-slide=count %}
