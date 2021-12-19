# Experiments

https://tufts.box.com/s/j12sbzunf4absbji9mt8oxeur9oaij2u

## StyleGAN2_ADA_Diamond_Kaggle_21-11-24

This experiment was run on 21-11-24 on Kaggle using StyleGAN2-ADA PyTorch (https://github.com/NVlabs/stylegan2-ada-pytorch) on the `diamonds-square` data. The outputs are from a version of `StyleGAN2_ADA_PyTorch_Kaggle.ipynb`.

## StyleGAN2_ADA_Diamond_Kaggle_21-11-27

This experiment was run on 21-11-27 on Kaggle using StyleGAN2 ADA PyTorch (https://github.com/NVlabs/stylegan2-ada-pytorch) on the `diamonds-square` data. This experiment resumed training on `network-snapshot-000400.pkl` from `StyleGAN2_ADA_Diamond_Kaggle_21-11-24`. Therefore, the file in this folder also named `network-snapshot-000400.pkl` could really be though of as version `000800`.

The outputs are from a version of `StyleGAN2_ADA_PyTorch_Kaggle.ipynb`.

## StyleGAN2_ADA_NOAUG_Diamond_Kaggle_21-12-01

This experiment was run on 21-12-01 on Kaggle using StyleGAN2 ADA PyTorch (https://github.com/NVlabs/stylegan2-ada-pytorch) on the `diamonds-square` data. We ran this experiment to try to see if setting `aug=noaug` would make the output models work with GANSpace (since GANSpace is not compatible with StyleGAN2-ADA). This did not end up working.

The outputs are from a version of `StyleGAN2_ADA_PyTorch_Kaggle.ipynb`.

## StyleGAN2_ADA_Gemstones_Angles_Kaggle_21-12-09

This experiment was run on 21-12-09 on Kaggle using StyleGAN2 ADA PyTorch (https://github.com/NVlabs/stylegan2-ada-pytorch) on the `gemstones_angled-square` data. The outputs are from a version of `StyleGAN2_ADA_PyTorch_Kaggle.ipynb`.

## StyleGAN2_PyTorch_Diamond_Kaggle_21-12-09

This experiment was run on 21-12-09 on Kaggle using StyleGAN2 (not ADA) PyTorch (https://github.com/rosinality/stylegan2-pytorch) on the `diamonds-square` data. We ran this experiment to so we could hopefully use the Closed-Form Factorization script. The outputs are from a version of `StyleGAN2_PyTorch_Kaggle.ipynb`.

### StyleGAN2_PyTorch_Diamond_CFF_9000

This experiment was run on `009000.pt` from `StyleGAN2_PyTorch_Diamond_Kaggle_21-12-09` using the closed form factorization scripts from https://github.com/rosinality/stylegan2-pytorch. The outputs are from a version of `StyleGAN2_PyTorch_Closed-Form-Factorization_Kaggle.ipynb`.

## StyleGAN2_ADA_Diamond_Transfer_Gemstones_Angled_Kaggle_21-12-09

This experiment was run on 21-12-09 on Kaggle using StyleGAN2 ADA PyTorch (https://github.com/NVlabs/stylegan2-ada-pytorch) on the `gemstones_angled-square` data. This experiment resumed training on `network-snapshot-000400.pkl` from `StyleGAN2_ADA_Diamond_Kaggle_21-11-24`, meaning that the model was initially trained on diamonds for 400 ticks, and then transferred learning to angled gemstones for 400 ticks.

The outputs are from a version of `StyleGAN2_ADA_PyTorch_Kaggle.ipynb`.

## StyleGAN2_PyTorch_Diamond_Transfer_Gemstones_Kaggle_21-12-10

This experiment was run on 21-12-10 on Kaggle using StyleGAN2 (not ADA) PyTorch (https://github.com/rosinality/stylegan2-pytorch) on the `gemstones_angled-square` data. This experiment resumed training on `009000.pt` from `StyleGAN2_PyTorch_Diamond_Kaggle_21-12-09`, meaning that the model was initially trained on diamonds for 9000 steps, and then transferred learning to angled gemstones for 9000 steps.

The outputs are from a version of `StyleGAN2_PyTorch_Kaggle.ipynb`.

### StyleGAN2_PyTorch_Diamond_Transfer_Gemstones_CFF_18000

This experiment was run on `018000.pt` from `StyleGAN2_PyTorch_Diamond_Transfer_Gemstones_Kaggle_21-12-10` using the closed form factorization scripts from https://github.com/rosinality/stylegan2-pytorch. The outputs are from a version of `StyleGAN2_PyTorch_Closed-Form-Factorization_Kaggle.ipynb`.

## StyleGAN2_PyTorch_9k_Diamond_18k_Gemstones_Kaggle_21-12-11

This experiment was run on 21-12-11 on Kaggle using StyleGAN2 (not ADA) PyTorch (https://github.com/rosinality/stylegan2-pytorch) on the `gemstones_angled-square` data. This experiment resumed training on `018000.pt` from `StyleGAN2_PyTorch_Diamond_Transfer_Gemstones_Kaggle_21-12-10`, meaning that the model was initially trained on diamonds for 9000 steps, and then transferred learning to angled gemstones for 18000 steps.

The outputs are from a version of `StyleGAN2_PyTorch_Kaggle.ipynb`.

### StyleGAN2_PyTorch_9k_Diamond_18k_Gemstones_CFF_27000

This experiment was run on `027000.pt` from `StyleGAN2_PyTorch_9k_Diamond_18k_Gemstones_Kaggle_21-12-11` using the closed form factorization scripts from https://github.com/rosinality/stylegan2-pytorch. The outputs are from a version of `StyleGAN2_PyTorch_Closed-Form-Factorization_Kaggle.ipynb`.

## StyleGAN2_PyTorch_9k_Diamond_27k_Gemstones_Kaggle_21-12-13

This experiment was run on 21-12-13 on Kaggle using StyleGAN2 (not ADA) PyTorch (https://github.com/rosinality/stylegan2-pytorch) on the `gemstones_angled-square` data. This experiment resumed training on `027000.pt` from `StyleGAN2_PyTorch_9k_Diamond_18k_Gemstones_Kaggle_21-12-11`, meaning that the model was initially trained on diamonds for 9000 steps, and then transferred learning to angled gemstones for 27000 steps.

The outputs are from a version of `StyleGAN2_PyTorch_Kaggle.ipynb`.

# Data

## Diamonds

### `diamonds_catalog.csv`

This CSV file contains data and features about all the diamond images downloaded around 2021-11-17. There are 20701 images.

### `diamonds-raw.zip`

This file contains the raw images of all the diamonds. Note that not all the images are square or the same size.

### `diamonds-square.zip`

This file contains the diamonds-raw images after running them through  `scraping/pad_and_resize.py`. The images are padded (if necessary) to be square and 256x256.

## Gemstones

### `gemstones_catalog.csv`

This CSV file contains data and features about all the gemstone images downloaded at 2021-12-08. There are 1178 images.

### `gemstones-raw.zip`

This file contains the raw images of all the gemstones.

### `gemstones-square.zip`

This file contains the gemstones-raw images after running them through  `scraping/pad_and_resize.py`. The images are padded (if necessary) to be square and 256x256.

### Gemstones Angled

### `gemstones_angled_catalog.csv`

This CSV file contains data and features about all the angled gemstone images downloaded at 2021-12-08. There are 37399 images.

### `gemstones_angled-raw.zip`

This file contains the raw images of all the angled gemstones.

### `gemstones_angled-square.zip`

This file contains the gemstones_angled-raw images after running them through  `scraping/pad_and_resize.py`. The images are padded (if necessary) to be square and 256x256.

# Closed Form Factorization

## Latent Space Interpolation Videos

This folder contains all of the output videos generated from the 027000 diamond model and 036000 gemstones model using `Kaggle/Closed_Form_Factoriztion_Kaggle.ipynb`.