<template>
    <div>
        <input type="text" v-model="url" />
        <button v-on:click="sendUrl">send</button>
    </div>
    <div class="progressBar">
       <div id="innerbar" class="innerbar"></div>
    </div>
    <div class="bar" v-for="(item, i) in getEmotion" v-bind:key="i">
        <div v-if="item === 'angry'" style="outline-style: solid; outline-color:white; background-color:red; color:red;" @click="changeImg(i)">a</div>
        <div v-if="item === 'happy'" style="outline-style: solid; outline-color:white; background-color:blue; color:blue; border-color:red" @click="changeImg(i)">a</div>
        <div v-if="item === 'surprise'" style="outline-style: solid; outline-color:white; background-color:green; color:green;" @click="changeImg(i)">a</div>
    </div>
    <div v-if="image">
        <img class="im" v-bind:src="'data:image/jpeg;base64,'+image"  />
    </div>
    
</template>

<script>

export default {
    name: 'MainPage',
    /*
    components: {
        ProgressBar
    },
    */
    data(){
        return {
            url: '',
            list: [],
            progress: 0,
            emotions: [],
            image: null,
            socket: null
            
        }
    },
    computed: {
        getEmotion() {
            console.log(this.list)
            return this.list.map((item) => Object.keys(item[0].emotions).reduce((a, b) => item[0].emotions[a] > item[0].emotions[b] ? a : b))
        },
    },
    watch: {
        progress: function(newProgress) {
            let el = document.getElementById("innerbar")
            console.log(newProgress + "%")
            el.style.width = newProgress + "%"
        }
    },
    methods: {
        sendUrl() {
            if (this.url) {
                this.socket.send(this.url)
            }
        },
        changeImg(i) {
            this.image = this.list[i][0].image
        },
        
    },
    created: function() {
        this.socket = new WebSocket("ws://61cd-35-203-131-19.ngrok.io/video") // server 입력
        this.socket.onmessage = (event) => {
            if (!isNaN(Number(event.data))) {
                this.progress = event.data
            }
            else {
                this.list = JSON.parse(event.data.replace(/'/g, '"')).data
            }
            
        }
    }
}
</script>

<style>
.bar {
    display: inline-flex;
    background: linear-gradient(#6fa6d66c, #7db1df54);
}
.progressBar {
  max-width: 330px;
  width: 90%;
  margin: 10px auto;
  height: 8px;

  border-radius: 3px;
  background: linear-gradient(#6fa6d66c, #7db1df54);
}

.innerbar {
  max-width: 330px;
  height: 100%;
  text-align: right;
  height: 8px; /* same as #progressBar height if we want text middle aligned */
  width: 0%;
  border-radius: 3px;
  background: linear-gradient(#5be6ba, #5ed1ad);
}

.im {
    width: 500px;
    height: 500px;
    object-fit: contain;
}
</style>