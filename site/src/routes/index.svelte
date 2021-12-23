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
    <Blanchor href="https://tufts.box.com/s/j12sbzunf4absbji9mt8oxeur9oaij2u">
      <button style="background-color:#FF5733;outline: none;border: none;color:white">
        All Output Files <Fa icon={faFile}/>
      </button>
    </Blanchor>
    &nbsp;

    <Blanchor href="https://tufts.box.com/s/ipm16ki7vfk7g0bt4v48mmcbgq0yav4b">
      <button style="background-color:#F39C12;outline: none;border: none;color:white">
        Full Report <Fa icon={faFilePdf}/>
      </button>
    </Blanchor>
    &nbsp;

    <Blanchor href="https://tufts.box.com/s/lqd4d4vvgmhg7spqkpap1y0izr94p4w9">
      <button style="background-color:#3498DB;outline: none;border: none;color:white">
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

    <h2>Controlling Output Features via Latent Space Eignvectors</h2>
    <br/>

    <h3>Diamonds 27k Training Iterations, 10 indices, 15 samples, 10 degrees</h3>
    <video width="100%" height="auto" controls style="background-color:gray">
      <source src="diamond_8-indices_15-samples_10-degrees_027000.mp4" type="video/mp4">
      Your browser does not support the video tag :( but you can view it <Blanchor href="https://tufts.box.com/s/srj3pfkonl3x36euxiz4ar4ibfni81li">here</Blanchor>
      <track kind="captions"/>
    </video>

    <br/>

    <h3>Gemstones 36k Training Iterations, 8 indices, 10 samples, 10 degrees</h3>
    <video width="100%" height="auto" controls style="background-color:gray">
      <source src="gemstones_8-indices_10-samples_10-degrees_036000.mp4" type="video/mp4">
      Your browser does not support the video tag :( but you can view it <Blanchor href="https://tufts.box.com/s/srj3pfkonl3x36euxiz4ar4ibfni81li">here</Blanchor>
      <track kind="captions"/>
    </video>

    <hr/>

    <h2>Sample Generated Images</h2>
    <br/>

    <h3>Diamonds, 27k Training Iterations</h3>
    <div>
      <img src="diamond_027000.png" alt="example generated diamond images"/>
    </div>

    <br/>

    <h3>Gemstones, 36k Training Iterations</h3>
    <div>
      <img src="gemstones_036000.png" alt="example generated gemstone images"/>
    </div>
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
    /* height: 70vh; */
	}
  @media only screen and (min-width: 600px) {
		header {
			/* height: 50vh; */
		}
	}

  img {
    width: 100%;
  }

  /* img {
    width: 100%;
  } */
</style>