import * as THREE from 'three';
import '../libs/inflate.module.min'
import {Zlib} from "../libs/inflate.module.min.js";
import FBXLoader from 'threejs-fbxloader';
import OrbitControls from 'three-orbitcontrols';
import Stats from '../libs/stats.module';
import * as dat from 'dat.gui';

let renderer,camera,scene,material,mesh,geometry,controls,light;
const gui = new dat.GUI();
let obj = initMesh();

function initRenderer() {
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth,window.innerHeight);
    document.body.appendChild(renderer.domElement)
}
function initScene() {
    scene = new THREE.Scene()
}
function initCamera() {
    camera = new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000)
    camera.position.z = 100;
    camera.position.y = 3;
    camera.position.x = 3;
}

function initMesh() {
    var pointsArr = [
        new THREE.Vector3( -10, 0, -5 ),
        new THREE.Vector3( -5, 15, 5 ),
        new THREE.Vector3( 20, 15, -5 ),
        new THREE.Vector3( 0, 15, -5 ),

    ];

    let lineGeometry = new THREE.BoxGeometry(10,10,10);
    material = new THREE.MeshPhongMaterial({color:0x00ffff}); //创建材质
    mesh = new THREE.Mesh(lineGeometry,material);
    return mesh;
}
function animate() {
    requestAnimationFrame(animate);
    obj.rotation.x +=0.01;
    obj.rotation.y +=0.01;
    renderer.render(scene,camera)
}
function addMesh() {
    obj.rotation.x = 120;
    scene.add(obj);
}
function initLight() {
    light = new THREE.DirectionalLight(0xffffff);
    light.position.set(20,50,50)
    // scene.add(light)
    scene.add(new THREE.AmbientLight(0x222222));
    let directionalLight = new THREE.DirectionalLight( 0xffffff, 0.5 );
    directionalLight.color.set(0xffffff);  //将光照颜色修改为黑色
    directionalLight.intensity = 2.0; //将光照强度修改为默认

    directionalLight.position.set(10, 10, 10); //设置平行光的位置
    scene.add( directionalLight );

}

function initGUI() {
    controls = {
        positionX:0,
        positionY:0,
        positionZ:0
    };
    gui.add(controls, "positionX", 0, 10).onChange(updatePosition);
    gui.add(controls, "positionY", 0, 10).onChange(updatePosition);
    gui.add(controls, "positionZ", 0, 10).onChange(updatePosition);
    function updatePosition() {
        obj.position.set(controls.positionX, controls.positionY, controls.positionZ);
    }

}
function init() {
    initRenderer();
    initScene();


    initLight();
    initCamera();
    initGUI();
    addMesh();
    animate();
}
window.onload = function () {
    init();
};
