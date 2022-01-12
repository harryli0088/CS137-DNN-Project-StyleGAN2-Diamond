<script lang="ts">
  import Blanchor from "$lib/Blanchor.svelte";
  import { base } from '$app/paths'
  import { faGithub } from "@fortawesome/free-brands-svg-icons";
  import Fa from "svelte-fa";
  import { faPlay, faRedo } from "@fortawesome/free-solid-svg-icons";

  type ImageData = {
    real: boolean,
    src: string,
  }

  const MAX_IMAGES = 100 // the maximum number of images in each class (ie real vs generated)
	const GAME_LENGTH = 10 //the number of images to quiz the player on

  enum GAME_STATE {
    IDLE,
    ASK,
    REVEAL,
    END,
  }

  let encounteredImages:ImageData[] = []
  let gameState = GAME_STATE.IDLE
  let score:number = 0
  let wasCorrect: boolean = false

  $: currentImage = encounteredImages.at(-1)

  function startGame() {
    //reset the game data
    encounteredImages = []
    score = 0
    
    nextQuestion() //add a new image
  }

  function nextQuestion() {
    if(encounteredImages.length < GAME_LENGTH) { //if the game has not ended yet
      addImage() //add an image
    }
    else {
      endGame() //else end the game
    }
  }

  const MAX_LOOPS = 1000 //used as a guardrail so we don't get forever loops
  function addImage() {
    let noForeverLoop = 0
    while(noForeverLoop < MAX_LOOPS) { //dumb while loop until we find an image we haven't used yet
      const imgData = randomlyPickImage() //randomly get an image
      if(encounteredImages.find(d => d.src === imgData.src) === undefined) { //if this is a new image
        encounteredImages = encounteredImages.concat(imgData) //add the new img data, use concat so svelte updates the state
        break //break out of the while loop
      }

      noForeverLoop++ //make sure we don't loop forever
    }

    if(noForeverLoop >= MAX_LOOPS) {
      console.error("No Forever Loop guardrail was triggered!")
    }

    gameState = GAME_STATE.ASK //ask the player about this image
  }

  function randomlyPickImage():ImageData {
    let real = Math.random() > 0.5 //randomly select whether to pick a real or fake image
    let imageNumber = Math.floor(100 * Math.random()) + 1 //randomly select a number from [1,100]

    return {
      real,
      src: `${base}/images/${real?"real":"generated"}/${imageNumber}.jpg`
    }
  }

  function answer(real:boolean) {
    gameState = GAME_STATE.REVEAL //reveal the answer to the user
    
    wasCorrect = real === currentImage.real //check if the player was correct
    if(wasCorrect) { //increment the score if the player was correct
      score += 1
    }
  }

  function endGame() {
    gameState = GAME_STATE.END
  }
</script>

<svelte:head>
	<title>Real vs Fake Diamonds Game</title>
</svelte:head>

<div id="game-container">
  <section>
    {#if gameState !== GAME_STATE.IDLE}
      <div>
        <h1>Image #{encounteredImages.length}</h1>

        <img src={currentImage.src} alt="is this real or generated?">

        <br/>

        {#if gameState === GAME_STATE.ASK}
          <p style="margin-bottom:0.5em">Is this image:</p>

          <div>
            <button class="colored" on:click={() => answer(true)} style="background-color:#28B463">Real</button>
            or 
            <button class="colored" on:click={() => answer(false)} style="background-color:#E74C3C">Generated</button>
            ?
          </div>

          <p>Score: {score} / {encounteredImages.length - 1}</p>
        {:else if gameState === GAME_STATE.REVEAL}
          <p style="margin-bottom:0.5em">
            {wasCorrect ? "Correct!" : "Incorrect."} {`This is a ${currentImage.real?"real":"generated"} diamond.`}
          </p>
          
          <button class="colored" on:click={() => nextQuestion()} style="background-color:#F39C12;">Next</button>

          <p>Score: {score} / {encounteredImages.length}</p>
        {:else if gameState === GAME_STATE.END}
          <p>Your final score was <b>{score} / {encounteredImages.length}</b></p>

          <button class="colored" on:click={() => startGame()} style="background-color:#F39C12;">Play Again <Fa icon={faRedo}/></button>
        {/if}
      </div>
    {:else}
      <div>
        <h1>
          Can you tell the difference between 
          <br/>
          real vs generated diamonds?
        </h1>

        <button class="colored" on:click={() => startGame()} style="background-color:#F39C12;">Start Game <Fa icon={faPlay}/></button>
      </div>
    {/if}
  </section>
</div>

<style>
  #game-container {
    text-align: center;
    display: flex;
    justify-content: center;
    height: 100vh;
    align-items: center;
    background-color: #2874A6;
    color: #fff;
  }
</style>
