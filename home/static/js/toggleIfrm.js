window.onload = function () {
    buscarIdMoodle();
    getAprenderCourses();
    changePage('Appcampus');

    // Obtenemos la referencia del carrusel
    var myCarousel = document.querySelector('#myCarousel')

    // Creamos un objeto de carrusel de Bootstrap
    var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 2000 // Cambiar el tiempo de transición de las imágenes en milisegundos
    })
};

var bodyAssignment = ``;

function changePage(pageToChange) {
    // Appcampus   home
    // AppMisCursos      controlEscolar
    // AppBiblioteca         dspace
    // AppEspaciosFisicos    AppEspaciosFisicos
    // AppEspaciosVirtuales    aulasVirtuales
    // AppAyuda     digitalizacionEmpresa

    var showDiv = "display: block !important;";
    var hideDiv = "display: none !important;";

    console.log(pageToChange);

    switch (pageToChange) {
        case 'Appcampus':
            document.getElementById(pageToChange).style.cssText = showDiv;
            document.getElementById('AppMisCursos').style.cssText = hideDiv;
            document.getElementById('AppBiblioteca').style.cssText = hideDiv;
            document.getElementById('AppEspaciosFisicos').style.cssText = hideDiv;
            document.getElementById('AppEspaciosVirtuales').style.cssText = hideDiv;
            document.getElementById('AppAyuda').style.cssText = hideDiv;
            break;
        case 'AppMisCursos':
            document.getElementById(pageToChange).style.cssText = showDiv;
            document.getElementById('Appcampus').style.cssText = hideDiv;
            document.getElementById('AppBiblioteca').style.cssText = hideDiv;
            document.getElementById('AppEspaciosFisicos').style.cssText = hideDiv;
            document.getElementById('AppEspaciosVirtuales').style.cssText = hideDiv;
            document.getElementById('AppAyuda').style.cssText = hideDiv;
            break;
        case 'AppBiblioteca':
            document.getElementById(pageToChange).style.cssText = showDiv;
            document.getElementById('Appcampus').style.cssText = hideDiv;
            document.getElementById('AppMisCursos').style.cssText = hideDiv;
            document.getElementById('AppEspaciosFisicos').style.cssText = hideDiv;
            document.getElementById('AppEspaciosVirtuales').style.cssText = hideDiv;
            document.getElementById('AppAyuda').style.cssText = hideDiv;
            break;
        case 'AppEspaciosFisicos':
            document.getElementById(pageToChange).style.cssText = showDiv;
            document.getElementById('Appcampus').style.cssText = hideDiv;
            document.getElementById('AppMisCursos').style.cssText = hideDiv;
            document.getElementById('AppBiblioteca').style.cssText = hideDiv; /////
            document.getElementById('AppAyuda').style.cssText = hideDiv;
            document.getElementById('AppEspaciosVirtuales').style.cssText = hideDiv;
            break;
        case 'AppEspaciosVirtuales':
            document.getElementById(pageToChange).style.cssText = showDiv;
            document.getElementById('Appcampus').style.cssText = hideDiv;
            document.getElementById('AppMisCursos').style.cssText = hideDiv;
            document.getElementById('AppBiblioteca').style.cssText = hideDiv;
            document.getElementById('AppEspaciosFisicos').style.cssText = hideDiv;
            document.getElementById('AppAyuda').style.cssText = hideDiv;
            break;
        case 'AppAyuda':
            document.getElementById(pageToChange).style.cssText = showDiv;
            document.getElementById('Appcampus').style.cssText = hideDiv;
            document.getElementById('AppMisCursos').style.cssText = hideDiv;
            document.getElementById('AppBiblioteca').style.cssText = hideDiv;
            document.getElementById('AppEspaciosFisicos').style.cssText = hideDiv;
            document.getElementById('AppEspaciosVirtuales').style.cssText = hideDiv;
            break;
        default:
            document.getElementById(pageToChange).style.cssText = hideDiv;
    }

}

const buscarIdMoodle = () => {
    // const emailUser = `{{request.user.email}}`;
    const emailUser = 'jemina.desantos@plai.mx';
    // const emailUser = 'daniel.romo@plai.mx';
    let calendarEl = document.getElementById('calendar');
    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'es',
    });
    calendar.render();
    const core_user_get_users_by_field = `https://pruebacampus.plai.mx/webservice/rest/server.php?wstoken=50eb47430a24daa3e4b78b42a71948e2&wsfunction=core_user_get_users_by_field&field=email&values[0]=${emailUser}&moodlewsrestformat=json`;
    fetch(core_user_get_users_by_field)
        .then(response => response.json())
        .then(data => {
            const IdMoodleUser = data[0].id;
            const getCEmail = data[0].email;
            const core_enrol_get_users_courses = `https://pruebacampus.plai.mx/webservice/rest/server.php?wstoken=50eb47430a24daa3e4b78b42a71948e2&wsfunction=core_enrol_get_users_courses&moodlewsrestformat=json&userid=${IdMoodleUser}`;
            fetch(core_enrol_get_users_courses)
                .then(response => response.json())
                .then(resCourses => {
                    contadorCursos = 0;
                    let contadorCompletos = 0;
                    let bodyCourses = ``;
                    let bodyEndedCourses = ``;
                    let idEvents = [];
                    let calendarEvents = [];
                    let bodyMyCoursesMoodle = ``;
                    for (const curso in resCourses) {
                        if (resCourses[curso].enddate != 0) {
                            const fechaActual = Math.floor(Date.now() / 1000);
                            // if (fechaActual < resCourses[curso].enddate) {
                                const unixTimestamp = resCourses[curso].enddate;
                                const date = new Date(unixTimestamp * 1000);
                                const year = date.getFullYear();
                                const month = ('0' + (date.getMonth() + 1)).slice(-2);
                                const day = ('0' + date.getDate()).slice(-2);
                                const formattedDate = `${day}/${month}/${year}`;
                                contadorCursos++;
                                let urlCurso = `https://pruebacampus.plai.mx/course/view.php?id=${resCourses[curso].id}`;
                                let imgCurso = '';
                                if (resCourses[curso].overviewfiles[0] && resCourses[curso].overviewfiles[0].fileurl) {
                                    let urlImagen = resCourses[curso].overviewfiles[0].fileurl;
                                    imgCurso = urlImagen.replace('/webservice', '');
                                } else {
                                    imgCurso = 'https://cognosnovedades.com/mailings/2020/sc/moodle/banner-moo.png';
                                }
                                let progreso = 0;
                                if (!resCourses[curso].progress) {
                                    progreso = parseFloat(progreso).toFixed(2)
                                } else {
                                    progreso = parseFloat(resCourses[curso].progress).toFixed(2);
                                }
                                bodyCourses += `
                                    <tr>
                                        <th>
                                            <div class="symbol symbol-50px me-2">
                                                <span class="fw-bold fs-9">${resCourses[curso].displayname}</span>
                                            </div>
                                        </th>
                                        <!--
                                        <td>
                                            <span class="fw-bold fs-9">10/10</span>
                                        </td>
                                        -->
                                        <td>
                                            <div class="d-flex flex-column w-100 me-2">
                                                <span class="fw-bold fs-9">${formattedDate}</span>
                                            </div>
                                        </td>
                                        <td class="text-end">
                                            <div class="d-flex flex-stack mb-2">
                                                <span class="fw-bold fs-9">${progreso}%</span>
                                            </div>
                                            <div class="progress h-6px w-100">
                                                <div class="progress-bar bg-primary" role="progressbar" style="width: ${resCourses[curso].progress}%" aria-valuenow="${resCourses[curso].progress}" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column w-100 me-2">
                                                <a style="cursor: pointer;" onclick="window.open('https://pruebacampus.plai.mx/course/view.php?id=${resCourses[curso].id}', '_blank');">
                                                    <span class="fs-9" style=" color: #cf1b6b !important;font-weight: 800;">Ver curso</span>
                                                </a>
                                            </div>
                                        </td>
                                </tr>`;
                                
                                if (contadorCursos <= 6) {
                                    bodyMyCoursesMoodle += `
                                    <div class="col-xs-12 col-md-4 pt-4">
                                        <div class="learn-card-container  ">
                                            <div class="learn-card-Moodle mb-1" style=" background: #f9f9f9;">
                                                <div class="bodyCard p-0">
                                                    <div class="flip-container" id="fc_">
                                                        <div class="flipper">
                                                            <div class="front">
                                                                <div class="parte1">
                                                                    <div class="tarjetas" style=" height: 150px; background-image: url('${imgCurso}');"></div>
                                                                    <div class="card-body card-body p-5">

                                                                        <div class="bodyCardTitle">
                                                                            <span style=" color: gray; ">Curso</span> </br>
                                                                            <span class="ejesTematicos" style=" font-weight: 700; ">${resCourses[curso].displayname}</span>
                                                                        </div>
                                                                        <div class="col-12">
                                                                            <div class="row row p-4">

                                                                                <div class="col-sm-12 p-0 pt-4">
                                                                                    <div class="d-flex flex-stack mb-2">
                                                                                        <span class="fw-bold fs-9">${progreso}%</span>
                                                                                    </div>
                                                                                    <div class="progress h-10px w-100" style=" background: #dedede; ">
                                                                                        <div class="progress-bar-moodle bg-primary" role="progressbar" style="width: ${resCourses[curso].progress}%" aria-valuenow="${resCourses[curso].progress}" aria-valuemin="0" aria-valuemax="100"></div>
                                                                                    </div>
                                                                                </div>

                                                                                <div class="col-sm-12 p-0 pt-4 d-flex justify-content-end">
                                                                                    <a onclick="window.open('https://pruebacampus.plai.mx/course/view.php?id=${resCourses[curso].id}', '_blank');">
                                                                                        <button type="button"
                                                                                            class="btn btnContinuar col-12 pts12">Continuar</button>
                                                                                    </a>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>`;

                                }
                                if (resCourses[curso].completed) {
                                    contadorCompletos ++;
                                    bodyEndedCourses += `
                                    <tr>
                                        <th>
                                            <div class="symbol symbol-50px me-2">
                                                <span class="fw-bold fs-9">${resCourses[curso].displayname}</span>
                                            </div>
                                        </th>
                                        <td>
                                            <div class="d-flex flex-column w-100 me-2">
                                                <span class="fw-bold fs-9">En curso</span>
                                            </div>
                                        </td>
                                        <td class="text-end">
                                            <div class="d-flex flex-stack mb-2">
                                                <span class="fw-bold fs-9">${progreso}%</span>
                                            </div>
                                            <div class="progress h-6px w-100">
                                                <div class="progress-bar bg-primary" role="progressbar" style="width: ${resCourses[curso].progress}%" aria-valuenow="${resCourses[curso].progress}" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column w-100 me-2">
                                                <a style="cursor: pointer;" onclick="window.open('https://pruebacampus.plai.mx/course/view.php?id=${resCourses[curso].id}', '_blank');">
                                                    <span class="fs-9">Ver curso</span>
                                                </a>
                                            </div>
                                        </td>
                                    </tr>`;
                                }
                                if (contadorCompletos === 0) {
                                    containerTableEndedCourses
                                    document.getElementById('containerTableEndedCourses').innerHTML = '<h6 class="text-muted py-5" style=" color: #cf1b6b!important;">Sin cursos finalizados</h6>';
                                }
                                // Trae el calendario
                                if (!resCourses[curso].completed) {
                                    const core_calendar_get_calendar_upcoming_view = `https://pruebacampus.plai.mx/webservice/rest/server.php?wstoken=50eb47430a24daa3e4b78b42a71948e2&wsfunction=core_calendar_get_calendar_upcoming_view&moodlewsrestformat=json&courseid=${resCourses[curso].id}`;
                                    fetch(core_calendar_get_calendar_upcoming_view)
                                        .then(response => response.json())
                                        .then(dataCalendar => {
                                            for (const event in dataCalendar.events) {
                                                if (!idEvents.includes(dataCalendar.events[event].id)) {
                                                    idEvents.push(dataCalendar.events[event].id);
                                                    const date = new Date(dataCalendar.events[event].timestart * 1000);
                                                    const year = date.getFullYear();
                                                    const month = ("0" + (date.getMonth() + 1)).slice(-2);
                                                    const day = ("0" + date.getDate()).slice(-2);
                                                    const formattedDate = year + "-" + month + "-" + day;
                                                    if (dataCalendar.events[event].timeduration > 0) {
                                                        const segundos = 691200;
                                                        const dias = segundos / (24 * 60 * 60);
                                                        const date = new Date(dataCalendar.events[event].timestart * 1000);
                                                        date.setDate(date.getDate() + dias);
                                                        const year = date.getFullYear();
                                                        const month = ("0" + (date.getMonth() + 1)).slice(-2);
                                                        const day = ("0" + date.getDate()).slice(-2);
                                                        const formattedDate2 = year + "-" + month + "-" + day;
                                                        var newEvent = {
                                                            title: dataCalendar.events[event].name,
                                                            start: formattedDate,
                                                            end: formattedDate2,
                                                            url: dataCalendar.events[event].viewurl
                                                        };
                                                    } else {
                                                        var newEvent = {
                                                            title: dataCalendar.events[event].name,
                                                            start: formattedDate,
                                                            url: dataCalendar.events[event].viewurl
                                                        };
                                                    }
                                                    calendar.addEvent(newEvent);
                                                }
                                            }
                                        }).catch(function (error) {
                                        });

                                    

                                    getAssigments(resCourses[curso].id, resCourses[curso].displayname);
                                }
                            // }
                        }

                    }
                    document.getElementById('bodyCardsMoodle').innerHTML = bodyMyCoursesMoodle;
                    if (contadorCursos > 4) {
                        document.getElementById("btnVerMas").style.display = "block";
                    }
                    document.getElementById('bodyCourses').innerHTML = bodyCourses;
                    document.getElementById('bodyEndedCourses').innerHTML = bodyEndedCourses;
                    getCalendarDates(calendarEvents);
                }).catch(function (error) {
                });
        });
}

const getAssigments = async (idCourse, nameCourse) => {
    const getAssignmentsUrl = `https://pruebacampus.plai.mx/webservice/rest/server.php?wstoken=50eb47430a24daa3e4b78b42a71948e2&wsfunction=mod_assign_get_assignments&moodlewsrestformat=json&courseids[0]=${idCourse}`;
    fetch(getAssignmentsUrl)
    .then(response => response.json())
    .then(assignment => {
        if (assignment.courses[0].assignments.length > 0) {
            for (const key in assignment.courses[0].assignments) {
                    const unixTimestamp = assignment.courses[0].assignments[key].duedate;
                    const date = new Date(unixTimestamp * 1000);
                    const year = date.getFullYear();
                    const month = ('0' + (date.getMonth() + 1)).slice(-2);
                    const day = ('0' + date.getDate()).slice(-2);
                    const formattedDate = `${day}/${month}/${year}`;
                    bodyAssignment += `
                        <p>
                            <span class="menu-link">
                                <span class="menu-icon">
                                    <i class="ki-duotone ki-teacher fs-2" style=" color: #005c9d;">
                                        <span class="path1"></span>
                                        <span class="path2"></span>
                                        <span class="path3"></span>
                                        <span class="path4"></span>
                                        <span class="path5"></span>
                                    </i>
                                </span>
                                <span class="menu-title" style=" color: #005c9d;"><b>${nameCourse}</b></span>
                            </span>
                            </br>
                            <span class="pl-4 text-muted" style=" padding-left: 25px;">
                                ${assignment.courses[0].assignments[key].name}
                            </span>
                            </br>
                            <span class="pl-4 text-muted" style=" padding-left: 25px;" >
                                <b>Vence el:</b>
                                ${formattedDate}
                            </span>
                        </p>
                    `;
                    document.getElementById('bodyAssginment').innerHTML = bodyAssignment;

                // Crear un objeto Date a partir del timestamp UNIX
                const fecha = new Date(unixTimestamp * 1000);
                // Configurar la zona horaria a GMT-6
                fecha.setUTCHours(fecha.getUTCHours() - 6);
                // Obtener la fecha y hora actual en GMT-6
                const ahora = new Date();
                // Comparar si la fecha ya ha pasado
                if (fecha < ahora) {
                    // console.log("La fecha "+formattedDate+" ya ha pasado en GMT-6");
                } else {
                    // console.log("La fecha "+formattedDate+" aún no ha pasado en GMT-6");
                }

            }   
        }
    }).catch(function (error) {
    });

}

const getAprenderCourses = () => {
    // fetch('https://aprender.plai.mx/api_programa/programas/', {
    //     method: 'GET',
    //     mode: 'cors'
    //   })
    //   .then(response => response.json())
    //     .then(yyy => {
    //       console.log(yyy);
    //       // Aquí puedes hacer lo que quieras con la respuesta obtenida
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    let simulateRes = {
        "count": 24,
        "next": "https://aprender.plai.mx/api_programa/programas/?limit=10&offset=10",
        "previous": null,
        "results": [
            {
                "pk": 61,
                "titulo": "1A067-023 VIVE LA REALIDAD VIRTUAL EN PLAI",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/portada_4Ct4ki4.png",
                "descripcion_general": "<p>En la actualidad, ha incrementado el inter&eacute;s por el campo de la realidad virtual y m&aacute;s porque este tipo de tecnolog&iacute;a se puede vincular con diversos proyectos y &aacute;reas de conocimiento, desde el sector p&uacute;blico, de salud y educativo, hasta los temas vinculados al emprendedurismo y la innovaci&oacute;n. Por estas razones, surge el presente taller enfocado en crear experiencias interactivas de VR&nbsp;con acompa&ntilde;amiento personalizado y mediante dispositivos m&oacute;viles, simuladores y visores especiales.</p>",
                "eje_tematico": {
                    "eje_tematico": "Industria 4.0"
                },
                "tipo": {
                    "tipo": "Taller"
                },
                "fecha_fin": "2023-02-16"
            },
            {
                "pk": 79,
                "titulo": "3B146-001 SAT PARA EMPRENDEDORAS",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/portada_1.png",
                "descripcion_general": "<p>Las participantes aprender&aacute;n los conocimientos b&aacute;sicos para formalizar su empresa ante el SAT.</p>",
                "eje_tematico": {
                    "eje_tematico": "Innovación y emprendimiento"
                },
                "tipo": {
                    "tipo": "Curso"
                },
                "fecha_fin": "2023-05-27"
            },
            {
                "pk": 8,
                "titulo": "4E060-001 PROGRAMA PLAI EDX: ONLINE CAMPUS ESSENTIALS",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/portadilla_CV_edX.png",
                "descripcion_general": "<p>Obt&eacute;n acceso a m&aacute;s de 100 cursos seleccionados en los temas m&aacute;s demandados y emergentes para el &eacute;xito acad&eacute;mico y profesional actual.&nbsp; <strong>Inscr&iacute;bete ahora.</strong></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Para acceder&nbsp;sigue estos pasos: ​&nbsp;</p>\r\n\r\n<ol>\r\n\t<li style=\"list-style-type:decimal\">Inscr&iacute;bete y espera tu correo de invitaci&oacute;n por parte de edX.&nbsp;</li>\r\n\t<li style=\"list-style-type:decimal\">Crea tu cuenta. Busca los cursos de tu inter&eacute;s e inscr&iacute;bete.&nbsp;</li>\r\n\t<li style=\"list-style-type:decimal\">Encontrar&aacute;s cursos de niveles: principiante, intermedio y avanzado.&nbsp;</li>\r\n\t<li style=\"list-style-type:decimal\">Organiza tus tiempos y horarios.&nbsp;</li>\r\n\t<li style=\"list-style-type:decimal\">Tendr&aacute;s hasta el 29 de junio de 2024 para completarlos. Finaliza con &eacute;xito tus cursos y <strong>obt&eacute;n tu certificados sin costo.</strong></li>\r\n</ol>\r\n\r\n<p>Prep&aacute;rate ahora en las habilidades del futuro. Inscr&iacute;bete en este programa ahora.</p>",
                "eje_tematico": {
                    "eje_tematico": "Tecnologías de la información"
                },
                "tipo": {
                    "tipo": "Programa"
                },
                "fecha_fin": "2024-06-29"
            },
            {
                "pk": 65,
                "titulo": "1B036-005 ENGLISH & INNOVATION. INTERMEDIATE COURSE",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/photo_4947643510442535803_y.jpg",
                "descripcion_general": "<p>Este curso aborda contenidos sobre tecnolog&iacute;a, innovaci&oacute;n y emprendimiento. Las tem&aacute;ticas centrales se manifiestan en cada competencia espec&iacute;fica.</p>",
                "eje_tematico": {
                    "eje_tematico": "Soft skills"
                },
                "tipo": {
                    "tipo": "Curso"
                },
                "fecha_fin": "2023-05-18"
            },
            {
                "pk": 55,
                "titulo": "3B055-029 HABILIDADES DIGITALES #ELLAHACEHISTORIA",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/portada.png",
                "descripcion_general": "<p>Aprende las herramientas que proporciona Meta para promocionar&nbsp;tu negocio en redes sociales&nbsp;</p>",
                "eje_tematico": {
                    "eje_tematico": "Innovación y emprendimiento"
                },
                "tipo": {
                    "tipo": "Taller"
                },
                "fecha_fin": "2023-02-11"
            },
            {
                "pk": 66,
                "titulo": "1B010-009 ENGLISH FOR SOFT SKILLS AT WORK. ADVANCED COURSE",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/photo_5100671060600269412_y_COaDZmh.jpg",
                "descripcion_general": "<p>&nbsp;</p>\r\n\r\n<p>Este curso busca mejorar el desempe&ntilde;o verbal y escrito en ingl&eacute;s y desarrollar habilidades de comunicaci&oacute;n aplicadas a ambientes laborales y acad&eacute;micos.</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>",
                "eje_tematico": {
                    "eje_tematico": "Soft skills"
                },
                "tipo": {
                    "tipo": "Curso"
                },
                "fecha_fin": "2023-03-30"
            },
            {
                "pk": 63,
                "titulo": "2C028-003 TRANSVERSALIDAD DEL CAMBIO CLIMÁTICO EN EL GOBIERNO DEL ESTADO DE JALISCO",
                "dependencia": "SEM",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/postal_aprender_SEMADET.png",
                "descripcion_general": "<p>Este diplomado surge de la necesidad para fortalecer las capacidades de las y los funcionarios p&uacute;blicos del Gobierno del Estado de Jalisco, que mediante la Comisi&oacute;n Interinstitucional de Cambio Clim&aacute;tico (CICC), remarca su compromiso para lograr las metas del Acuerdo de Par&iacute;s. Por esta raz&oacute;n, la Secretar&iacute;a de Medio Ambiente y Desarrollo Sustentable (SEMADET) y la Secretar&iacute;a de Innovaci&oacute;n, Ciencia y Tecnolog&iacute;a (SICyT), a trav&eacute;s de la Plataforma Abierta de Innovaci&oacute;n y de Desarrollo de Jalisco (PLAi) se coordinaron para la realizaci&oacute;n de este programa.</p>",
                "eje_tematico": {
                    "eje_tematico": "Innovación y emprendimiento"
                },
                "tipo": {
                    "tipo": "Diplomado"
                },
                "fecha_fin": "2023-06-22"
            },
            {
                "pk": 80,
                "titulo": "3A059-001 ORACLE CLOUD INFRASTRUCTURE FOUNDATIONS I",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/portada_SJto3w1.png",
                "descripcion_general": "<p>Este curso aborda conceptos b&aacute;sicos, t&eacute;rminos e ideas centrales de la infraestructura de ORACLE Cloud en cuatro ejes: Core Infrastructure, Database, Solutions, Platform and Edge y Governance and Administration.</p>",
                "eje_tematico": {
                    "eje_tematico": "Tecnologías de la información"
                },
                "tipo": {
                    "tipo": "Curso"
                },
                "fecha_fin": "2023-07-19"
            },
            {
                "pk": 50,
                "titulo": "3B039-017 PROGRAMA BÁSICO DE INCLUSIÓN DIGITAL",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/portada_sandbox_inclusion_digital.png",
                "descripcion_general": "<p>Este curso ofrece contenido digital para un aprendizaje autogestivo y muestra el uso de herramientas digitales de forma productiva, responsable y segura.</p>\r\n\r\n<p>&nbsp;</p>",
                "eje_tematico": {
                    "eje_tematico": "Tecnologías de la información"
                },
                "tipo": {
                    "tipo": "Curso"
                },
                "fecha_fin": "2023-03-10"
            },
            {
                "pk": 62,
                "titulo": "1A082-084 TALLER CREA TU ROBOT EN PLAI",
                "dependencia": "P",
                "estatus": "Activo",
                "imagen_programa": "https://aprender.plai.mx/media/programas/imagenes/portada_taller_robotica23.png",
                "descripcion_general": "<p>&quot;PLAi en su deber de contribuir y acelerar la capacitaci&oacute;n de capital humano para cubrir las demandas de los trabajos actuales y del futuro en Jalisco, impulsando la competitividad del sector productivo y promoviendo la innovaci&oacute;n, realiz&oacute; un taller de Rob&oacute;tica para conocer su esencia y aplicaciones.</p>",
                "eje_tematico": {
                    "eje_tematico": "Industria 4.0"
                },
                "tipo": {
                    "tipo": "Taller"
                },
                "fecha_fin": "2023-02-15"
            }
        ]
    }
    let bodyAprenderCourse = '';
    let bodyMyCourses = '';
    let cont = 0;
    let activeCard = '';
    let liCarouselItem = '';
    for (const key in simulateRes.results) {
        if (cont < 1) {
            activeCard = ' active ';
            activeLi = ' class="active" ';
        } else {
            activeCard = '';
            activeLi = '';
        }
        bodyAprenderCourse += `
            <div class="carousel-item ${activeCard} ">
                <div class="col-md-12 pt-4">
                    <div class="learn-card-container animate__animated animate__fadeInUp ">
                        <div class="learn-card mb-1" style=" background: #f9f9f9;">
                            <div class="bodyCard p-0">
                                <div class="flip-container" id="fc_">
                                    <div class="flipper">
                                        <div class="front">
                                            <div class="parte1">
                                                <div class="tarjetas" style=" height: 150px; background-image: url('${simulateRes.results[key].imagen_programa}');"></div>
                                                <div class="col-sm-12 m-0 tipoProgramaTitulo row align-items-center">
                                                    <div class="col-12 text-center">
                                                        <span class="ejesTematicos">${simulateRes.results[key].eje_tematico.eje_tematico}</span>
                                                    </div>
                                                </div>
                                                <div class="card-body">
                                                    <div class="bodyCardTitle">
                                                        <h6 class="titleCard fs-8 text-muted text-muted-plai fw-semibold">${simulateRes.results[key].titulo}</h6>
                                                    </div>
                                                    <div class="col-12">
                                                        <div class="row align-items-center">
                                                            <div class="col-sm-12 p-0 pt-4">
                                                                <a href="https://sandbox.plai.mx/">
                                                                    <button type="button"
                                                                        class="btn btnInscripcion col-12 pts12">Consultar oferta disponible</button>
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        if (cont <= 5) {
            bodyMyCourses += `
            <div class="col-xs-12 col-md-4 pt-4">
                <div class="learn-card-container animate__animated animate__fadeInUp ">
                    <div class="learn-card mb-1" style=" background: #f9f9f9;">
                        <div class="bodyCard p-0">
                            <div class="flip-container" id="fc_">
                                <div class="flipper">
                                    <div class="front">
                                        <div class="parte1">
                                            <div class="tarjetas" style=" height: 150px; background-image: url('${simulateRes.results[key].imagen_programa}');"></div>
                                            <div class="col-sm-12 m-0 tipoProgramaTitulo row align-items-center">
                                                <div class="col-12 text-center">
                                                    <span class="ejesTematicos">${simulateRes.results[key].eje_tematico.eje_tematico}</span>
                                                </div>
                                            </div>
                                            <div class="card-body p-5 m-5">
                                                <div class="bodyCardTitle">
                                                    <h6 class="titleCard fs-8 text-muted text-muted-plai fw-semibold">${simulateRes.results[key].titulo}</h6>
                                                </div>
                                                <div class="col-12 mt-5 pt-5">
                                                    <div class="row align-items-center">
                                                        <div class="col-sm-12 p-0 pt-4">
                                                            <a href="https://sandbox.plai.mx/">
                                                                <button type="button"
                                                                    class="btn btnInscripcion col-12 pts12">Consultar oferta disponible</button>
                                                            </a>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`;
        }
        liCarouselItem += `
            <li data-bs-target="#myCarousel" data-bs-slide-to="${cont}" ${activeLi} ></li>
        `;
        cont ++;
    } 
    document.getElementById('courseItems').innerHTML = bodyAprenderCourse;
    document.getElementById('liCarousel').innerHTML = liCarouselItem;
    document.getElementById('bodyCards').innerHTML = bodyMyCourses;
}
