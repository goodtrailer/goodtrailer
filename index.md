---
layout: base
title: home
assets: /assets/index/
carousels:
  - images:
    - path: /assets/index/20220905_142805.jpg
    - path: /assets/index/20220912_172358.jpg
    - path: /assets/index/20220915_171654.jpg
    - path: /assets/index/20230414_225138.jpg
    - path: /assets/index/20230616_161726.jpg
    - path: /assets/index/20230709_102845.jpg
    - path: /assets/index/20230729_191855.jpg
    - path: /assets/index/20230819_145037.jpg
    - path: /assets/index/20230822_155733.jpg
    - path: /assets/index/20230909_113747.jpg
    - path: /assets/index/20230917_142838.jpg
    - path: /assets/index/20231125_124518.jpg
    - path: /assets/index/20240120_033120.jpg
    - path: /assets/index/20240322_185813.jpg
    - path: /assets/index/20240616_083017.jpg
    - path: /assets/index/20240707_120032.jpg
    - path: /assets/index/20240907_085624.jpg
    - path: /assets/index/20240928_191339.jpg
    - path: /assets/index/20241003_102528.jpg
    - path: /assets/index/20241101_225522.jpg
    - path: /assets/index/20241105_220025.jpg
    - path: /assets/index/20241111_104352.jpg
    - path: /assets/index/20241203_161504.jpg
    - path: /assets/index/20241226_152038.jpg
    - path: /assets/index/20250312_173110.jpg
    - path: /assets/index/20250525_190635.jpg
    - path: /assets/index/20250616_150945.jpg
    - path: /assets/index/20250705_131609.jpg
    - path: /assets/index/20250831_151701.jpg
    - path: /assets/index/20250901_141304.mp4
      video: true
    - path: /assets/index/20251121_182006.jpg
    - path: /assets/index/20251218_105500.jpg
    - path: /assets/index/20251224_203218.jpg
    - path: /assets/index/20260219_203530.jpg
    dimensions:
    - width: 4000.0
      height: 3000.0
    - width: 4000.0
      height: 3000.0
    - width: 4000.0
      height: 3000.0
    - width: 3000.0
      height: 2250.0
    - width: 3000.0
      height: 4000.0
    - width: 4000.0
      height: 3000.0
    - width: 4000.0
      height: 3000.0
    - width: 3000.0
      height: 4000.0
    - width: 3000.0
      height: 4000.0
    - width: 4000.0
      height: 3000.0
    - width: 4000.0
      height: 3000.0
    - width: 4000.0
      height: 3000.0
    - width: 3000.0
      height: 2250.0
    - width: 3968.0
      height: 2976.0
    - width: 2208.0
      height: 2944.0
    - width: 3822.0
      height: 2867.0
    - width: 4000.0
      height: 3000.0
    - width: 3825.0
      height: 2868.0
    - width: 3000.0
      height: 4000.0
    - width: 3000.0
      height: 4000.0
    - width: 4000.0
      height: 3000.0
    - width: 2208.0
      height: 2944.0
    - width: 2539.0
      height: 4000.0
    - width: 3000.0
      height: 4000.0
    - width: 2793.0
      height: 2793.0
    - width: 3958.0
      height: 2968.0
    - width: 3000.0
      height: 4000.0
    - width: 4000.0
      height: 3000.0
    - width: 5920.0
      height: 2800.0
    - width: 1080.0
      height: 1920.0
    - width: 2992.0
      height: 2992.0
    - width: 2884.0
      height: 2884.0
    - width: 3000.0
      height: 4000.0
    - width: 2992.0
      height: 2992.0
    captions:
    - 9/05/2022, 2:28pm
    - 9/12/2022, 5:23pm
    - 9/15/2022, 5:16pm 
    - 4/14/2023, 10:51pm &mdash; kamiya's blue whale
    - 6/16/2023, 4:17pm
    - 7/09/2023, 10:28am
    - 7/29/2023, 7:18pm
    - 8/19/2023, 2:50pm
    - 8/22/2023, 3:57pm
    - 9/09/2023, 11:37am
    - 9/17/2023, 2:28pm 
    - 11/25/2023, 12:45pm
    - 1/20/2024, 3:31am &mdash; kamiya's little bird
    - 3/22/2024, 6:58pm
    - 6/16/2024, 8:30am
    - 7/07/2024, 12:00pm
    - 9/07/2024, 8:56am
    - 9/28/2024, 7:13pm
    - 10/03/2024, 10:25am &mdash; kamiya's pegasus
    - 11/01/2024, 10:55pm
    - 11/05/2024, 10:00pm &mdash; bioluminescence
    - 11/11/2024, 10:43am
    - 12/03/2024, 4:15pm &mdash; hojyo's violinist
    - 12/26/2024, 3:20pm
    - 3/12/2025, 5:31pm &mdash; kamiya's praying mantis
    - 5/22/2025, 7:06pm
    - 6/16/2025, 3:09pm
    - 7/05/2025, 1:16pm
    - 8/31/2025, 3:17pm
    - 9/01/2025, 2:13pm
    - 11/21/2025, 6:20pm &mdash; lang's crane on a plane (krishna ver.)
    - 12/18/2025, 10:55pm
    - 12/24/2025, 8:32pm
    - 2/19/2026, 8:35pm &mdash; kato's shiba inu
---

{% assign count = page.carousels[0].images.size | minus: 1 %}
{% include carousel.html max-height="555" number="1" first-slide=count %}
