<script lang="ts">
  import Fa from 'svelte-fa'
  import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'
  import { faFilePdf } from '@fortawesome/free-solid-svg-icons'
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
    </div>
  </header>

  <section>
    <!-- <a href="Interactive_Visual_Uncertainty_Quantification_Poster.pdf" target="_blank" rel="noopener noreferrer">
      <button style="background-color:#FF5733;outline: none;border: none;color:white">
        Full Poster <Fa icon={faFilePdf}/>
      </button>
    </a>
    &nbsp;
    <a href="Interactive_Visual_Uncertainty_Quantification_Abstract.pdf" target="_blank" rel="noopener noreferrer">
      <button style="background-color:#F39C12;outline: none;border: none;color:white">
        Full Abstract <Fa icon={faFilePdf}/>
      </button>
    </a>
    &nbsp; -->
    
    <!-- <button style="background-color:rgb(29, 155, 240);border-radius:50%">
      <Blanchor href="https://twitter.com/VizSec/status/1449746373927075840" style="color:white">
        <Fa icon={faTwitter}/>
      </Blanchor>
    </button> -->

    <h2>Diamonds 27k Training Iterations, 10 indices, 15 samples, 10 degrees</h2>
    <video width="100%" height="auto" controls style="background-color:gray">
      <source src="diamond_8-indices_15-samples_10-degrees_027000.mp4" type="video/mp4">
      Your browser does not support the video tag :( but you can view it <Blanchor href="https://tufts.box.com/s/srj3pfkonl3x36euxiz4ar4ibfni81li">here</Blanchor>
      <track kind="captions"/>
    </video>

    <h2>Gemstones 36k Training Iterations, 8 indices, 10 samples, 10 degrees</h2>
    <video width="100%" height="auto" controls style="background-color:gray">
      <source src="gemstones_8-indices_10-samples_10-degrees_036000.mp4" type="video/mp4">
      Your browser does not support the video tag :( but you can view it <Blanchor href="https://tufts.box.com/s/srj3pfkonl3x36euxiz4ar4ibfni81li">here</Blanchor>
      <track kind="captions"/>
    </video>
  </section>
</main>

<style>
	header {
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;
		background-color: #17202A;
		color: white;
    text-align: center;
    height: 70vh;
	}
  @media only screen and (min-width: 600px) {
		header {
			height: 50vh;
		}
	}

  /* img {
    width: 100%;
  } */
</style>