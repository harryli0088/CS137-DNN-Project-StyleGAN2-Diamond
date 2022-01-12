<script lang="ts">
  import Fa from 'svelte-fa'
  import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'
  import { faFilePdf, faFile, faVideo } from '@fortawesome/free-solid-svg-icons'
  import Blanchor from '$lib/Blanchor.svelte';
</script>

<main>
	<header>
    <div>
      <h1>Training StyleGAN2 and Applying Latent Space Discovery Techniques on a Novel Gemstone Images Dataset</h1>
      <div>Harry X. Li, Marco Pretell</div>
      <br/>
      <div style="font-size:2em">
        <Blanchor href="https://github.com/harryli0088/CS137-DNN-Project-StyleGAN2-Diamond">
          <Fa class="icon-button" icon={faGithub} style="color:white;"/>
        </Blanchor>
      </div>

      <br/>

      <div>
        <img src="gemstones_index-13_degree-10.0.png" alt="example generated gemstone images"/>
      </div>
    </div>
  </header>

  <section>
    <p>We trained <Blanchor href="https://github.com/rosinality/stylegan2-pytorch">StyleGAN2</Blanchor> on a novel gemstone images dataset and applied a latent space discovery technique to control for output features. All the images and videos on this page are generated using an AI model.</p>

    <Blanchor href="https://tufts.box.com/s/j12sbzunf4absbji9mt8oxeur9oaij2u">
      <button class="colored" style="background-color:#FF5733">
        All Output Files <Fa icon={faFile}/>
      </button>
    </Blanchor>
    &nbsp;

    <Blanchor href="https://tufts.box.com/s/ipm16ki7vfk7g0bt4v48mmcbgq0yav4b">
      <button class="colored" style="background-color:#F39C12">
        Full Report <Fa icon={faFilePdf}/>
      </button>
    </Blanchor>
    &nbsp;

    <Blanchor href="https://tufts.box.com/s/lqd4d4vvgmhg7spqkpap1y0izr94p4w9">
      <button class="colored" style="background-color:#3498DB">
        Full Presentation <Fa icon={faVideo}/>
      </button>
    </Blanchor>
    &nbsp;
    
    <!-- <button style="background-color:rgb(29, 155, 240);border-radius:50%">
      <Blanchor href="https://twitter.com/VizSec/status/1449746373927075840" style="color:white">
        <Fa icon={faTwitter}/>
      </Blanchor>
    </button> -->

    <hr/>

    <h2>Sample Generated Images</h2>

    <p>These are sample output images from a model trained on a diamonds dataset and an angled gemstones dataset. Each cell represents one image generated from input noise.</p>

    <h3>Diamonds, 27k Training Iterations</h3>
    <div>
      <img src="diamond_027000.png" alt="example generated diamond images"/>
    </div>

    <br/>

    <h3>Gemstones, 36k Training Iterations</h3>
    <div>
      <img src="gemstones_036000.png" alt="example generated gemstone images"/>
    </div>

    <hr/>

    <h2>Controlling Output Features via Latent Space Eignvectors</h2>
    
    <p>We used a <Blanchor href="https://arxiv.org/abs/2007.06600">closed-form factorization</Blanchor> technique to identify eigenvectors in the latent space that control for output features. Each row (y axis) represents an eigenvector to be manipulated. The first row has the largest eigenvalue, and each subsequent row has smaller eignvalues. Each column (x axis) represents images generated using the same input noise vector. Change in time represents the change in manipulation intensity of the respective eigenvector from highly negative manipulation (early in the video), to no manipulation (middle of video), to highly positive manipulation (end of video). You can see that in the middle of the video when there is no manipulation, all the output images for a single column are the same.</p>

    <p>In most cases, we found that individual eigenvectors controlled multiple output features, making it tricky to explain. If you think you've discovered a good explanation for any of the eigenvectors, let us know by opening an issue in our <Blanchor href="https://github.com/harryli0088/CS137-DNN-Project-StyleGAN2-Diamond">repository</Blanchor>!</p>

    <h3>Diamonds 27k Training Iterations, 10 indices, 15 samples, 10 degrees</h3>

    <p>The 1st eigenvector (row) seems to decide whether the output diamond has a circular vs ovular shape. For example, when the manipulation is highly negative, the output shapes seem to be compact Rounds, Princesses (squares), and Hearts. When the manipulation is highly positive, the shapes are more elongated Ovals, Emeralds (rectangles), and Pears.</p>

    <p>Interestinly, the 2nd eigenvector (row) seems to control for centering and padding. In our dataset, some images needed to be centered and gray-padded into square dimensions. With negative manipulation, all the output images have our centering and padding artifacts. With positive manipulation, none of the images are centered or padded.</p>

    <video width="100%" height="auto" controls style="background-color:gray">
      <source src="diamond_8-indices_15-samples_10-degrees_027000.mp4" type="video/mp4">
      Your browser does not support the video tag :( but you can view it <Blanchor href="https://tufts.box.com/s/srj3pfkonl3x36euxiz4ar4ibfni81li">here</Blanchor>
      <track kind="captions"/>
    </video>

    <br/>

    <h3>Gemstones 36k Training Iterations, 8 indices, 10 samples, 10 degrees</h3>

    <p>The 2nd eigenvector (row) seems to decide whether the output gemstone is green and from a frontal angle (negative manipulation) vs pink and from a sideways angle (positive manipulation).</p>

    <p>The 3rd eigenvector (row) seems to decide whether the output gemstone is yellow (negative manipulation) or blue (positive manipulation).</p>

    <video width="100%" height="auto" controls style="background-color:gray">
      <source src="gemstones_8-indices_10-samples_10-degrees_036000.mp4" type="video/mp4">
      Your browser does not support the video tag :( but you can view it <Blanchor href="https://tufts.box.com/s/srj3pfkonl3x36euxiz4ar4ibfni81li">here</Blanchor>
      <track kind="captions"/>
    </video>
  </section>
</main>

<style>
  img {
    width: 100%;
  }
</style>