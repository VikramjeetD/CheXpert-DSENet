# DSENet - CheXpert
This project builds and uses the DenseNet with SE optimization to diagnose chest X-Rays. The CheXpert dataset ([available from the official website](https://stanfordmlgroup.github.io/competitions/chexpert/)) is used for the purpose.
In accordance with the dataset use agreement, no data files are uploaded. To run the code, you must get access to the dataset and change the filepaths accordingly.

Check out `test.ipynb` for model evaluation results and `visualization.ipynb` for a look at the visualizations of the model results.
An official submission has been made with the name "DSENet" towards the official competition (visible on the leaderboard).

# Possible improvements
- Try out different ways to handle the "unsure" labels, as proposed by the authors of the paper.
- Train an ensemble. Almost all of the top submissions to the competition are ensemble models.
- Better (and more "automated") hyperparam tuning. This was tedious due to timeout restrictions on Google Colab.
- Train on higher resolution images. Here, 224 x 224 images were used. The original paper uses 320 x 320. Higher resolution of images would give better results.
