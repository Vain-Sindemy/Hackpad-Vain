# Hackpad-Vain

Mon premier HackPad simple de 3 touches :
- Alt + Tab
- Alt + Shift + Tab
- Win + D

Premièrement, le SCH :

  <img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151320" src="https://github.com/user-attachments/assets/d28d7945-c36d-4b2a-a956-497809cce23a" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151310" src="https://github.com/user-attachments/assets/24905ed0-6447-40be-ad04-437c6c4f33a0" />

SCH Test :

<img width="582" height="764" alt="Capture d&#39;écran 2026-02-05 230609" src="https://github.com/user-attachments/assets/de137508-3f9b-491f-9b05-72c9d79d7941" />


Deuxièmement, le PCB finalisé:

<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151130" src="https://github.com/user-attachments/assets/995b5245-54a2-4a09-803d-a1b04cc845a8" />
<img width="339" height="664" alt="Capture d&#39;écran 2026-02-08 151120" src="https://github.com/user-attachments/assets/6aa60046-8ecc-434a-ab2e-4f56c7d02b8b" />

PCB Test :

<img width="973" height="832" alt="Capture d&#39;écran 2026-02-06 001156" src="https://github.com/user-attachments/assets/7b2cc8f7-1834-4333-a320-8832ada8f6fa" />
<img width="973" height="832" alt="Capture d&#39;écran 2026-02-06 001156" src="https://github.com/user-attachments/assets/e1f19592-cc93-4aa9-996d-3d8b595521c5" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-05 231550" src="https://github.com/user-attachments/assets/e79e3fce-8bc4-4958-a367-dc828a89f7a1" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-05 230913" src="https://github.com/user-attachments/assets/8e1f9532-3123-4b9a-b277-d9dade70078a" />


 Troisièmement, le Rendu 3D finalisé : 

 <img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151144" src="https://github.com/user-attachments/assets/abaafb45-5240-4da1-bc98-81966d528977" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151222" src="https://github.com/user-attachments/assets/fbe66025-e75b-4db6-b8eb-9bb01e693192" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151215" src="https://github.com/user-attachments/assets/b0efe5e5-d2e0-4139-8b3f-6d47bef31256" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151203" src="https://github.com/user-attachments/assets/4469a64f-6a01-44ba-93dd-f0cc57f7743e" />


 3D Test :

 <img width="1246" height="744" alt="Capture d&#39;écran 2026-02-06 002434" src="https://github.com/user-attachments/assets/76b077af-9aba-47b0-b66a-6ea3aaa9836f" />
<img width="1909" height="1076" alt="Capture d&#39;écran 2026-02-06 002213" src="https://github.com/user-attachments/assets/a5dc209a-d8dd-4a76-8b54-2d1764028218" />

 
 Quatrièmement, Coque et couvercle 3D :

 <img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151056" src="https://github.com/user-attachments/assets/bea45658-c6ce-4631-b2bf-11e4f17ae3b0" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151046" src="https://github.com/user-attachments/assets/9d7da683-8269-400b-82fd-d86e70f4dc5d" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151033" src="https://github.com/user-attachments/assets/41ce6a3a-06cc-4012-ad79-e7aad8aa7ec2" />
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-02-08 151106" src="https://github.com/user-attachments/assets/dc3fff91-05ce-4b9e-8886-7738b98db810" />


Notes personnelles sur mon expérience + Explications de problèmes :

Le projet proposé est super mais le processus est moins amusant que je ne le pensais.
Je m'explique, on me pose les 3 étapes à suivre mais on ne m'explique pas comment installer les différents programmes.
Pour KiCad, le Zip proposé que j'ai téléchargé et importé, mais sans explications c'était un calvaire à faire fonctionner.
Heureusement j'ai réussi bien que sur les dernières versions / version Windows OS et non Apple OS les étiquettes ne soient pas les mêmes, notamment pour assigner des empreintes.
De plus pour retourner le PCB, à cause du problème précédent le tuto n'a pas été d'une grande aide mais j'ai réussi.

Pour Fusion 360, j'ai utilisé Autodesk Fusion car c'est le seul que j'ai réussi à mettre sans trop de difficultés bien qu'il faille que je désactive mon DNS pour pouvoir utiliser le logiciel, créant quelques bugs pour me connecter et commencer à créer.
Le tuto proposé est bien sauf pour le couvercle que j'ai dû faire à la main puisque "ai03's plate generator" fonctionne avec "["","",""]" qui est propre à votre création.
J'ai personnellement dû le faire à partir de rien puisque le mien n'est pas exactement comme le vôtre.

Pour QMK Firmware, bien que ça ne relève pas de vous c'est aussi peu intuitif.

Mais le plus gros problème à mes yeux est GITHUB !
Personnellement c'était la première fois que je l'utilisais (avec la création d'un jeu Sprig "SIN EATER") et c'était vraiment compliqué de mettre tous les bons dossiers ensemble.
La prise en main est compliquée car peu expliquée pour moi.

Cependant, il n'y a pas que des problèmes ou points négatifs au contraire !
Je me suis beaucoup amusé à designer le PCB ainsi que la coque 3D.
Comprendre, essayer et réussir sont une partie intégrante de mon premier projet.
