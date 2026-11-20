# Bengali Deep News Summarization (BANS)

An attention-based Sequence-to-Sequence neural network for abstractive Bengali news summarization using LSTM networks.

This repository implements the research presented in our Springer publication, **Bengali Abstractive News Summarization (BANS): A Neural Attention Approach**.

## Model Architecture

- LSTM-based Encoder-Decoder architecture
- Neural Attention Mechanism
- Sequence-to-Sequence learning
- Vocabulary-based Bengali text processing
- Greedy decoding for summary generation

## Technologies

- Python
- TensorFlow 1.x
- NumPy
- Pandas
- NLTK

## Repository Structure

```text
Bengali-Deep-News-Summarization/
├── Data-Manipulation/
├── Result_Analysis/
├── dataset/
├── output/
├── data_utils.py
├── seq2seq_model.py
├── execute.py
├── evaluation.py
├── seq2seq.ini
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/Prithwiraj12/Bengali-Deep-News-Summarization.git
cd Bengali-Deep-News-Summarization
```

Install dependencies in a compatible legacy TensorFlow environment. The original implementation uses TensorFlow 1.x APIs and is not directly compatible with TensorFlow 2.x.

## Dataset

The model uses paired Bengali news articles and their corresponding headlines or summaries. Training, evaluation, and test files are organized under the `dataset/` directory.

Ensure that the source articles and target summaries are line-aligned and configure their paths in `seq2seq.ini`.

## Running the Model

Configure the execution mode in `seq2seq.ini`:

**Training:**
```ini
mode = train
```

```bash
python execute.py
```

**Testing:**
```ini
mode = test
```

```bash
python execute.py
```

**Interactive Summarization:**
```ini
mode = interactive
```

```bash
python execute.py
```

Generated summaries are saved to the configured output location.

## Publication

**Bengali Abstractive News Summarization (BANS): A Neural Attention Approach**

Prithwiraj Bhattacharjee, Avi Mallick, Md. Saiful Islam, and Marium-E-Jannat.

*Proceedings of International Conference on Trends in Computational and Cognitive Engineering*, pp. 41–51, Springer, 2021.

- **DOI:** https://doi.org/10.1007/978-981-33-4673-4_4
- **Paper:** [Springer Link](https://link.springer.com/chapter/10.1007/978-981-33-4673-4_4)
- **Preprint:** [arXiv:2012.01747](https://arxiv.org/abs/2012.01747)

### BibTeX

```bibtex
@inproceedings{bhattacharjee2020bengali,
  title={Bengali abstractive news summarization (BANS):
         a neural attention approach},
  author={Bhattacharjee, Prithwiraj and
          Mallick, Avi and
          Saiful Islam, Md. and
          Marium-E-Jannat},
  booktitle={Proceedings of International Conference on
             Trends in Computational and Cognitive Engineering:
             Proceedings of TCCE 2020},
  pages={41--51},
  year={2020},
  organization={Springer}
}
```

## Author

**Prithwiraj Bhattacharjee**  
Assistant Professor, Department of Computer Science and Engineering  
Leading University, Sylhet, Bangladesh.

- GitHub: https://github.com/Prithwiraj12
- Website: https://prithwiraj12.github.io/

## License

See the [LICENSE](LICENSE) file for details.
