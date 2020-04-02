import * as THREE from 'three';
// import '../libs/inflate.min.js'
// import {Zlib} from "../libs/inflate.module.min.js";
import FBXLoader from 'threejs-fbxloader';
import OrbitControls from 'three-orbitcontrols';
// import Stats from '../libs/stats.module';
// import * as dat from 'dat.gui';

// const gui = new dat.GUI();
FBXLoader(THREE);

let container,
    stats,
    controls,
    renderEnabled=true;
let camera, scene, renderer, light;
let clock = new THREE.Clock();
let dragonTipBtn = document.querySelector('.dragon-tip');

let mixer;
let action;
let model;
let timmer;
let animationState = true;
let timeOut = null;
let textureImgUrl ='./img/texture/';
let textureList = [
    [
        new THREE.TextureLoader().load(textureImgUrl+"5.png"),
        new THREE.TextureLoader().load(textureImgUrl+"DragoEyes.png")
    ],
    [   new THREE.TextureLoader().load(textureImgUrl+"2.png"),
        new THREE.TextureLoader().load(textureImgUrl+"DragoEyes.png")
    ],
    [   new THREE.TextureLoader().load(textureImgUrl+"3.png"),
        new THREE.TextureLoader().load(textureImgUrl+"DragoEyes.png")
    ],
    [   new THREE.TextureLoader().load(textureImgUrl+"4.png"),
        new THREE.TextureLoader().load(textureImgUrl+"DragoEyes.png")
    ]
];

export function staticAction() {
    console.log(animationState + '动画状态');
    // if (animationState&&action){
    //     return
    // }
    if (action) {
        action.stop();
    }
    clearTimeout(timmer);
    action = mixer.clipAction(model.animations[0]);
    // action.setLoop(THREE.LoopOnce,1);
    // action.time = 4;
    action.timeScale = 0.5;
    action.play();
    // action = mixer.clipAction(model.animations[1]);
    // action.play();

    animationState = action.isRunning()
    // timmer = setInterval(function () {
    //     animationState = action.isRunning()
    //     staticAction()
    // },200)
}

export function actionOneFun() {
    clearTimeout(timmer);
    action.stop();
    action = mixer.clipAction(model.animations[1]);
    action.time = 12.4;
    action.play();

    timmer = setTimeout(function () {
        action.stop();
        staticAction()
    }, 5500)

}

export function actionTwoFun() {
    clearTimeout(timmer);
    action.stop();
    action = mixer.clipAction(model.animations[2]);
    action.time = 18.16;
    action.play();
    timmer = setTimeout(function () {
        action.stop();
        staticAction()
    }, 23000);
}

export function actionThreeFun() {
    clearTimeout(timmer);
    action.stop();
    action = mixer.clipAction(model.animations[3]);
    action.time = 32;
    action.play();
    timmer = setTimeout(function () {
        action.stop();
        staticAction()
    }, 13000)
}

export function actionFourFun() {
    clearTimeout(timmer);
    action.stop();
    action = mixer.clipAction(model.animations[4]);
    action.time = 44.4;
    action.play();
    timmer = setTimeout(function () {
        action.stop();
        staticAction()
    }, 19000)
}

function initCamera() {
    camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 2000);
    camera.position.set(100, 200, 300);
}

function initScene() {
    scene = new THREE.Scene();
    scene.fog = new THREE.Fog(0xa0a0a0, 20, 1400);
}

function initLight() {

    light = new THREE.HemisphereLight(0xffffff, 0x444444, 1.2);
    light.position.set(0, 200, 0);
    scene.add(light);

    light = new THREE.DirectionalLight(0xffffff, 1.2);
    light.position.set(0, 200, 100);
    light.castShadow = true;
    light.shadow.camera.top = 180;
    light.shadow.camera.bottom = -100;
    light.shadow.camera.left = -120;
    light.shadow.camera.right = 120;
    scene.add(light);

}

export function deleteGroup() {
    if (!model){
        return
    }
    model.traverse(function (item) {
        if (item instanceof THREE.Mesh) {
            item.geometry.dispose(); //删除几何体
            item.material.dispose(); //删除材质
        }
    });

    scene.remove(model);
}

export function changeTexture(num) {
    let bodyTexture = checklvl(num);
    deleteGroup();
    model.traverse(function (child) {
        if (child.isMesh) {
            if (child.name === "SeaDragonBodY") {
                child.material.map = bodyTexture[0];
            }
            if (child.name === "Eyes") {
                child.material.map = bodyTexture[1];
            }
            child.castShadow = true;
            child.receiveShadow = true;
        }
    });
    setTimeout(function () {
        staticAction();
    }, 200);
    scene.add(model);
}

function checklvl(num) {

    if (15 >= num && num >= 1) {
        return textureList[0];
    }
    if (50 >= num && num >= 16) {
        return textureList[1];
    }
    if (80 >= num && num >= 51) {
        return textureList[2];
    }
    if (150 >= num && num >= 81) {
        return textureList[3];
    }
}

export async function initLoaderModule(num) {
    let loader = new THREE.FBXLoader();
    let temp;
    await loader.load('img/end.fbx', function (object) {
        dragonTipBtn.style.display = 'none';
        model = object;
        mixer = new THREE.AnimationMixer(model);
        temp = checklvl(num);
        object.traverse(function (child) {
            if (child.isMesh) {
                console.log(child);
                if (child.name === "SeaDragonBodY") {
                    child.material.map = temp[0];
                    child.castShadow = true;
                    child.receiveShadow = true;
                }
            if (child.name === "Eyes") {
                child.material.map = temp[1];
            }

            }
        });
        setTimeout(function () {
            staticAction();
        }, 200);
        object.position.y = 15;
        scene.add(object);
    }, function onProgress(xhr) {
        console.log('加载' + (xhr.loaded / xhr.total * 100) + '%');
        dragonTipBtn.style.display = 'block';

        if ((xhr.loaded / xhr.total * 100).toFixed(2)>0.9){
            dragonTipBtn.innerHTML = '模型渲染中';
            dragonTipBtn.style.left = document.documentElement.clientWidth / 2 - dragonTipBtn.offsetWidth / 2 + 'px';
        } else {
            dragonTipBtn.innerHTML = '加载' + (xhr.loaded / xhr.total * 100).toFixed(2) + '%';
            dragonTipBtn.style.left = document.documentElement.clientWidth / 2 - dragonTipBtn.offsetWidth / 2 + 'px';
        }
    });
}

    function initGround() {
        // let mesh = new THREE.Mesh(new THREE.PlaneBufferGeometry(2000, 2000), new THREE.MeshPhongMaterial({
        //     color: 0xFFF0EBE6,
        //     depthWrite: false
        // }));
        // mesh.rotation.x = -Math.PI / 2;
        // mesh.receiveShadow = true;
        // scene.add(mesh);
    let geometry;
    let ground;
    let material;
    geometry = new THREE.BoxBufferGeometry(400, 200, 400);
    material = new THREE.ShadowMaterial({opacity: 0.5});
    // material = new THREE.MeshNormalMaterial();
    material.opacity = 0.5;
    ground = new THREE.Mesh(geometry, material);
    ground.position.y = -85;
    ground.receiveShadow = true;
    scene.add(ground);
}

function initHelper() {
    let grid = new THREE.GridHelper(2000, 20, 0x000000, 0x000000);
    grid.material.opacity = 0.2;
    grid.material.transparent = true;
    scene.add(grid);


    controls = new OrbitControls(camera, renderer.domElement);
    controls.target.set(0, 100, 0);
    controls.update();
    controls.enableZoom = true;
    controls.enableDamping = true;
    //锁定x轴
    controls.minPolarAngle = Math.PI / 2;
    controls.maxPolarAngle = Math.PI / 2;
    controls.enablePan = true;

}

function initRender() {
    container = document.querySelector('#dragon');
    renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight * 0.7);
    renderer.shadowMap.enabled = true;
    container.appendChild(renderer.domElement);
}

function init() {

    initRender();
    initCamera();
    initScene();
    initLight();

    // ground
    initGround();
    initHelper();
    // model
    //  initLoaderModule();


}

// function onWindowResize() {
//     camera.aspect = renderer.domElement.clientWidth / renderer.domElement.clientHeight;
//     camera.updateProjectionMatrix();
//     renderer.setSize(window.innerWidth, window.innerHeight);
// }


function animate() {
    camera.aspect = renderer.domElement.clientWidth / renderer.domElement.clientHeight;
    camera.updateProjectionMatrix();
    let delta = clock.getDelta();
    if (mixer) mixer.update(delta);
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}
init();
animate();
