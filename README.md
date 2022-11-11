# Gated-ViGAT: Efficient bottom-up event recognition and explanation using a new frame selection policy and gating mechanism

This repository hosts the code and data for our paper: N. Gkalelis, D. Daskalakis, V. Mezaris, "Gated-ViGAT: Efficient bottom-up event recognition and explanation using a new frame selection policy and gating mechanism", IEEE International Symposium on Multimedia (ISM), Naples, Italy, Dec. 2022.

## Introduction
In this repository we provide the materials for Gated-ViGAT: an extension of our previously proposed method ViGAT [1] with a new frame selection policy and a gating mechanism.
In contrast to ViGAT, the proposed Gated-ViGAT extracts bottom-up information from only a small fraction of the sampled frames, as shown in the figure below. In this example, Gated-ViGAT correctly classifies both videos, belonging to the events Rafting (top row) and Snowboarding (bottom row), using only three frames (i.e. the ones shown within a green rectangle) derived using our new frame selection policy.

  ![methodIllustration](https://user-images.githubusercontent.com/33573818/201292360-e78a6667-63f5-48f8-8678-b3ffc7df9247.jpg)

The proposed frame selection policy utilizes an explanation and a dissimilarity measure to select the frames that better represent the event depicted in the video as well as provide a diverse overview of it.

Additionally, in Gated-ViGAT we introduce a gating mechanism that combines both convolution and attention in order to be able to process sequences of frames (contrarily to the CNN-based gating mechanism of [2], which only processes individual frames) and thus capture more effectively both the short- and long-term dependencies of the event occurring in the video.
Consequently, the proposed method continues to achieve high recognition performance, as ViGAT, but with a significant computational complexity reduction.
Lastly, contrarily to efficient top-down approaches, Gated-ViGAT can provide explanations about the classification outcome.

## Gated-ViGAT traning and evaluation procedures

### Code requirements

* numpy
* scikit-learn
* PyTorch

### Video preprocessing

The dataset root directory must contain the following subdirectories:
 * ```vit_global/```: Numpy arrays of size 30x768 (or 120x768) containing the global frame feature vectors for each video (the 30 (120) frames, times the 768-element vector for each frame).
  * ```vit_local/```: Numpy arrays of size 30x50x768 (or 120x50x768) containing the appearance feature vectors of the detected frame objects for each video (the 30 (120) frames, times the 50 most-prominent objects identified by the object detector, times a 768-element vector for each object bounding box).

For more informations extracting or obtaining these features please see the GitHub repository referring to our previous work: <a href="https://github.com/bmezaris/ViGAT" target="_blank">ViGAT: Bottom-up event recognition and explanation in video using factorized graph attention network [1]</a>.

Furthermore, in order to train Gated-ViGAT on any video-dataset, the corresponding ViGAT model should be present. 
The models for ActivityNet [2] and miniKinetics [3] are available inside ```weights/``` folder.

### Training

To train a new gate, utilizing our frame selection policy, run 
```
python train_gate.py weights/<vigat model>.pt --dataset_root <dataset dir> --dataset [<actnet|minikinetics>]
```

The training parameters can be modified by specifying the appropriate command line arguments. For more information, run ```python train_gate.py --help```.

### Evaluation

To evaluate a gate, run
```
python evaluation_gate.py weights/<vigat model>.pt weights/<model name>.pt --dataset_root <dataset dir> --dataset [<actnet|minikinetics>]
```
Τhe evaluation parameters can be modified by specifying the appropriate command line arguments. For more information, run ```python evaluation_gate.py --help```.



## License
This code is provided for academic, non-commercial use only. Please also check for any restrictions applied in the code parts and datasets used here from other sources (e.g. provided datasets [3,4]). Redistribution and use in source and binary forms, with or without modification, are permitted for academic non-commercial use provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation provided with the distribution. This software is provided by the authors "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. In no event shall the authors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

## Citation

If you find Gated-ViGAT code useful in your work, please cite the following publication where this approach was proposed:

N. Gkalelis, D. Daskalakis, V. Mezaris, "Gated-ViGAT: Efficient bottom-up event recognition and explanation using a new frame selection policy and gating mechanism", IEEE International Symposium on Multimedia (ISM), Naples, Italy, Dec. 2022.

BibTex:
```
@inproceedings{GatedViGAT_ISM2022,
author={Gkalelis, Nikolaos and Daskalakis, Dimitrios and Mezaris, Vasileios},
title={{Gated-ViGAT}: Efficient bottom-up event recognition and explanation using a new frame selection policy and gating mechanism},
year={2022},
month={Dec.},
booktitle={IEEE International Symposium on Multimedia (ISM)}
}
```

You may want to also consult and, if you find it useful, also cite our earlier work on this topic (ViGAT):

N. Gkalelis, D. Daskalakis, V. Mezaris, "ViGAT: Bottom-up event recognition and explanation in video using factorized graph attention network", IEEE Access, vol. 10, pp. 108797-108816, 2022. DOI: 10.1109/ACCESS.2022.3213652. https://doi.org/10.1109/ACCESS.2022.3213652

Bibtex:
```
@ARTICLE{ViGAT_Access22,
  author={Gkalelis, Nikolaos and Daskalakis, Dimitrios and Mezaris, Vasileios},
  journal={IEEE Access}, 
  title={ViGAT: Bottom-Up Event Recognition and Explanation in Video Using Factorized Graph Attention Network}, 
  year={2022},
  volume={10},
  number={},
  pages={108797-108816},
  doi={10.1109/ACCESS.2022.3213652},
  url={https://doi.org/10.1109/ACCESS.2022.3213652}    
}
```


## Acknowledgements

This work was supported by the EU Horizon 2020 programme under grant agreement 101021866 (CRiTERIA).

## References

[1] N. Gkalelis, D. Daskalakis, V. Mezaris, "ViGAT: Bottom-up event recognition and explanation in video using factorized graph attention network", IEEE Access, 2022. <a href="https://doi.org/10.1109/ACCESS.2022.3213652" target="_blank"> DOI: 10.1109/ACCESS.2022.3213652</a>.

[2] A. Ghodrati, B. Ehteshami Bejnordi and A. Habibian. FrameExit: Conditional Early Exiting for Efficient Video Recognition. In Proc. IEEE CVPR, 2021, pp. 15603-15613.

[3] B. G. Fabian Caba Heilbron, Victor Escorcia and J. C. Niebles. ActivityNet: A large-scale video benchmark for human activity understanding. In Proc. IEEE CVPR, 2015, pp. 961–970.

[4]  Saining Xie, Chen Sun, Jonathan Huang, Zhuowen Tu and Kevin Murphy. Rethinking Spatiotemporal Feature Learning: Speed-Accuracy Trade-offs in Video Classification. In Proc. ECCV, 2018, pp. 305-321.
