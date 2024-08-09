// Drop Down Script
$('select').on('change', function () {
  if ($(this).val()) {
    $(this).addClass('selected_item')
    $(this).find(':selected').addClass('selected_item_font')
  } else {
    $(this).removeClass('selected_item')
  }
})

$('#id_master_project').on('change', function () {
  if (!$(this).val()) {
    $('#id_project_name').removeClass('selected_item')
    $('#id_building_name').removeClass('selected_item')
  }
})

$('#id_project_name').on('change', function () {
  if (!$(this).val()) {
    $('#id_building_name').removeClass('selected_item')
  }
})

$('#id_property_type').on('change', function () {
  if (!$(this).val()) {
    $('#id_rooms_number').removeClass('selected_item')
  }
})

$(document).ready(function () {
  $('#id_master_project').select2()
  $('#id_master_project').on('select2:select', (e) => {
    htmx.trigger('#id_master_project', 'select2.select')
  })
})

function mousePointer(e) {
  let $canvas = document.getElementById('refresh-icon')
  $canvas.addEventListener('mouseover', function (e) {
    if (e.ctrlKey) {
      $canvas.style.cursor = 'none'
    } else {
      $canvas.style.cursor = 'pointer'
    }
  })
}

mousePointer()

function refreshFilters() {
  let url = new URL(window.location.href)
  window.location.href = url.origin + url.pathname
}
// let url = new URL(window.location.href)
// windows.location.raplace(url.origin + url.pathname)
window.history.replaceState(null, '', '/latest_transactions/')

// Button with alerts

$('#dialog_community').hide()
$('#dialog_project').hide()
$('#dialog_type').hide()
$('#all_transactions_button').on('click', function (e) {
  let target = $(this)
  let url = new URL(window.location.href)
  let selectedMasterProject = url.searchParams.get('master_project')
  let selectedProjectName = url.searchParams.get('project_name')
  let selectedPropertyType = url.searchParams.get('property_type')
  if (selectedMasterProject == null) {
    $('#dialog_community').dialog({
      height: 70,
      width: 350,
      modal: true,
      resizable: false,
      dialogClass: 'alert-dialog',
      position: {
        my: 'center',
        at: 'center',
        of: target,
      },
    })
    e.preventDefault()
    // alert('Please Choose a Community')
  } else if (selectedProjectName == null) {
    $('#dialog_project').dialog({
      height: 70,
      width: 350,
      modal: true,
      resizable: false,
      dialogClass: 'alert-dialog',
      position: {
        my: 'center',
        at: 'right',
        of: target,
      },
    })
    e.preventDefault()
  } else if (selectedPropertyType == null) {
    $('#dialog_type').dialog({
      height: 70,
      width: 350,
      modal: true,
      resizable: false,
      dialogClass: 'alert-dialog',
      position: {
        my: 'center',
        at: 'right',
        of: target,
      },
    })
    e.preventDefault()
  }
})

// Home Page
getHomePage()

function getHomePage() {
  let url = new URL(window.location.href)
  if (url.searchParams.size === 0) {
    $.ajax({
      method: 'GET',
      url: 'https://www.dxbstates.com/latest_transactions',
      data: {
        master_project: null,
        project_name: null,
        building_name: null,
        property_type: null,
        rooms_number: null,
        time_period: null,
      },
      xhrFields: {
        withCredentials: true,
      },
      async: false,
      cache: false,
      success: $.ajax({
        method: 'GET',
        data: {
          master_project: null,
          project_name: null,
          building_name: null,
          property_type: null,
          rooms_number: null,
          time_period: null,
        },
        url: "{% url 'ajax_url' %}",
        xhrFields: {
          withCredentials: true,
        },
        success: function (data) {
          console.log(data.master_project)
          console.log(data.project_name)
          console.log(data.building_name)
          console.log(data.property_type)
          console.log(data.rooms_number)
          console.log(data.time_period)
        },
        error: function (error_data) {
          console.log(error_data)
        },
      }),
    })

    // if (selectedChart) {
    //   selectedChart.destroy()
    // }
    // if (selectedBar) {
    //   selectedBar.destroy()
    // }

    // load_graph_data()
    // load_bar_data()
  }
}

function getProjectName() {
  let masterProject = document.getElementById('id_master_project')

  let selectedMasterProject = masterProject.value

  let masterProjectIndex = masterProject.selectedIndex
  let selectedMasterProjectName = masterProject.options[masterProjectIndex].text
  let titleBar = document.getElementById('title_bar')

  if (selectedMasterProjectName && selectedMasterProjectName !== 'Community') {
    titleBar.innerHTML = `Last 10 transactions in ${selectedMasterProjectName}`
  } else {
    titleBar.innerHTML = 'Last 10 transactions in Dubai'
  }

  let url = new URL(window.location.href)
  if (selectedMasterProject.length > 0) {
    url.searchParams.set('master_project', selectedMasterProject)
  } else {
    document.getElementById('id_building_name').options.length = 0
    document.getElementById('id_building_name').options[0] = new Option('Choose Building Name')
    url.searchParams.delete('building_name')
    url.searchParams.delete('project_name')
    url.searchParams.delete('master_project')
  }

  history.pushState({}, '', url.href)

  // let selectedMasterProject = url.searchParams.get('master_project')
  let selectedProjectName = url.searchParams.get('project_name')
  let selectedBuildingName = url.searchParams.get('building_name')
  let selectedPropertyType = url.searchParams.get('property_type')
  let selectedRoomsNumber = url.searchParams.get('rooms_number')
  let selectedTimePeriod = url.searchParams.get('time_period')

  $.ajax({
    method: 'GET',
    url: 'https://www.dxbstates.com/latest_transactions',
    data: {
      master_project: selectedMasterProject,
      project_name: selectedProjectName,
      building_name: selectedBuildingName,
      property_type: selectedPropertyType,
      rooms_number: selectedRoomsNumber,
      time_period: selectedTimePeriod,
    },
    xhrFields: {
      withCredentials: true,
    },
    async: false,
    cache: false,
    success: $.ajax({
      method: 'GET',
      data: {
        master_project: selectedMasterProject,
        project_name: selectedProjectName,
        building_name: selectedBuildingName,
        property_type: selectedPropertyType,
        rooms_number: selectedRoomsNumber,
        time_period: selectedTimePeriod,
      },
      url: "{% url 'ajax_url' %}",
      xhrFields: {
        withCredentials: true,
      },
      success: function (data) {
        console.log(data.master_project)
        console.log(data.project_name)
        console.log(data.building_name)
        console.log(data.property_type)
        console.log(data.rooms_number)
      },
      error: function (error_data) {
        console.log(error_data)
      },
    }),
  })

  // element.scrollTop = position

  if (selectedChart) {
    selectedChart.destroy()
  }
  if (selectedBar) {
    selectedBar.destroy()
  }

  load_graph_data()
  load_bar_data()
}

function getBuildingName() {
  let selectedProjectName = document.getElementById('id_project_name').value
  let url = new URL(window.location.href)
  if (selectedProjectName.length > 0) {
    url.searchParams.set('project_name', selectedProjectName)
  } else {
    url.searchParams.delete('building_name')
    url.searchParams.delete('project_name')
  }

  history.pushState({}, '', url.href)

  let selectedMasterProject = url.searchParams.get('master_project')
  // let selectedProjectName = url.searchParams.get('project_name')
  let selectedBuildingName = url.searchParams.get('building_name')
  let selectedPropertyType = url.searchParams.get('property_type')
  let selectedRoomsNumber = url.searchParams.get('rooms_number')
  let selectedTimePeriod = url.searchParams.get('time_period')

  $.ajax({
    method: 'GET',
    url: 'https://www.dxbstates.com/latest_transactions',
    data: {
      master_project: selectedMasterProject,
      project_name: selectedProjectName,
      building_name: selectedBuildingName,
      property_type: selectedPropertyType,
      rooms_number: selectedRoomsNumber,
      time_period: selectedTimePeriod,
    },
    xhrFields: {
      withCredentials: true,
    },
    async: false,
    cache: false,
    success: $.ajax({
      method: 'GET',
      data: {
        master_project: selectedMasterProject,
        project_name: selectedProjectName,
        building_name: selectedBuildingName,
        property_type: selectedPropertyType,
        rooms_number: selectedRoomsNumber,
        time_period: selectedTimePeriod,
      },
      url: "{% url 'ajax_url' %}",
      xhrFields: {
        withCredentials: true,
      },
      success: function (data) {
        console.log(data.master_project)
        console.log(data.project_name)
        console.log(data.building_name)
        console.log(data.property_type)
        console.log(data.rooms_number)
      },
      error: function (error_data) {
        console.log(error_data)
      },
    }),
  })

  if (selectedChart) {
    selectedChart.destroy()
  }
  if (selectedBar) {
    selectedBar.destroy()
  }

  // console.log('$$$$$$$')
  // console.log(data)
  load_graph_data()
  load_bar_data()
}

function listBuildingName() {
  let selectedBuildingName = document.getElementById('id_building_name').value
  let url = new URL(window.location.href)
  url.searchParams.set('building_name', selectedBuildingName)
  history.pushState({}, '', url.href)

  let selectedMasterProject = url.searchParams.get('master_project')
  let selectedProjectName = url.searchParams.get('project_name')
  // let selectedBuildingName = url.searchParams.get('building_name')
  let selectedPropertyType = url.searchParams.get('property_type')
  let selectedRoomsNumber = url.searchParams.get('rooms_number')
  let selectedTimePeriod = url.searchParams.get('time_period')

  $.ajax({
    method: 'GET',
    url: 'https://www.dxbstates.com/latest_transactions',
    data: {
      master_project: selectedMasterProject,
      project_name: selectedProjectName,
      building_name: selectedBuildingName,
      property_type: selectedPropertyType,
      rooms_number: selectedRoomsNumber,
      time_period: selectedTimePeriod,
    },
    xhrFields: {
      withCredentials: true,
    },
    async: false,
    cache: false,
    success: $.ajax({
      method: 'GET',
      data: {
        master_project: selectedMasterProject,
        project_name: selectedProjectName,
        building_name: selectedBuildingName,
        property_type: selectedPropertyType,
        rooms_number: selectedRoomsNumber,
        time_period: selectedTimePeriod,
      },
      url: "{% url 'ajax_url' %}",
      xhrFields: {
        withCredentials: true,
      },
      success: function (data) {
        console.log(data.master_project)
        console.log(data.project_name)
        console.log(data.building_name)
        console.log(data.property_type)
        console.log(data.rooms_number)
      },
      error: function (error_data) {
        console.log(error_data)
      },
    }),
  })

  if (selectedChart) {
    selectedChart.destroy()
  }
  if (selectedBar) {
    selectedBar.destroy()
  }

  load_graph_data()
  load_bar_data()
}

function getRoomsNumber() {
  let selectedPropertyType = document.getElementById('id_property_type').value
  let url = new URL(window.location.href)
  console.log(selectedPropertyType.length)
  if (selectedPropertyType.length > 0) {
    url.searchParams.set('property_type', selectedPropertyType)
  } else {
    url.searchParams.delete('rooms_number')
    url.searchParams.delete('property_type')
  }
  history.pushState({}, '', url.href)

  let selectedMasterProject = url.searchParams.get('master_project')
  let selectedProjectName = url.searchParams.get('project_name')
  let selectedBuildingName = url.searchParams.get('building_name')
  // let selectedPropertyType = url.searchParams.get('property_type')
  let selectedRoomsNumber = url.searchParams.get('rooms_number')
  let selectedTimePeriod = url.searchParams.get('time_period')

  $.ajax({
    method: 'GET',
    url: 'https://www.dxbstates.com/latest_transactions',
    data: {
      master_project: selectedMasterProject,
      project_name: selectedProjectName,
      building_name: selectedBuildingName,
      property_type: selectedPropertyType,
      rooms_number: selectedRoomsNumber,
      time_period: selectedTimePeriod,
    },
    xhrFields: {
      withCredentials: true,
    },
    async: false,
    cache: false,
    success: $.ajax({
      method: 'GET',
      data: {
        master_project: selectedMasterProject,
        project_name: selectedProjectName,
        building_name: selectedBuildingName,
        property_type: selectedPropertyType,
        rooms_number: selectedRoomsNumber,
        time_period: selectedTimePeriod,
      },
      url: "{% url 'ajax_url' %}",
      xhrFields: {
        withCredentials: true,
      },
      success: function (data) {
        console.log(data.master_project)
        console.log(data.project_name)
        console.log(data.building_name)
        console.log(data.property_type)
        console.log(data.rooms_number)
      },
      error: function (error_data) {
        console.log(error_data)
      },
    }),
  })

  if (selectedChart) {
    selectedChart.destroy()
  }
  if (selectedBar) {
    selectedBar.destroy()
  }

  load_graph_data()
  load_bar_data()
}

function listRoomsNumber() {
  let selectedRoomsNumber = document.getElementById('id_rooms_number').value
  let url = new URL(window.location.href)
  url.searchParams.set('rooms_number', selectedRoomsNumber)
  history.pushState({}, '', url.href)

  let selectedMasterProject = url.searchParams.get('master_project')
  let selectedProjectName = url.searchParams.get('project_name')
  let selectedBuildingName = url.searchParams.get('building_name')
  let selectedPropertyType = url.searchParams.get('property_type')
  // let selectedRoomsNumber = url.searchParams.get('rooms_number')
  let selectedTimePeriod = url.searchParams.get('time_period')

  $.ajax({
    method: 'GET',
    url: 'https://www.dxbstates.com/latest_transactions',
    data: {
      master_project: selectedMasterProject,
      project_name: selectedProjectName,
      building_name: selectedBuildingName,
      property_type: selectedPropertyType,
      rooms_number: selectedRoomsNumber,
      time_period: selectedTimePeriod,
    },
    xhrFields: {
      withCredentials: true,
    },
    async: false,
    cache: false,
    success: $.ajax({
      method: 'GET',
      data: {
        master_project: selectedMasterProject,
        project_name: selectedProjectName,
        building_name: selectedBuildingName,
        property_type: selectedPropertyType,
        rooms_number: selectedRoomsNumber,
        time_period: selectedTimePeriod,
      },
      url: "{% url 'ajax_url' %}",
      xhrFields: {
        withCredentials: true,
      },
      success: function (data) {
        console.log(data.master_project)
        console.log(data.project_name)
        console.log(data.building_name)
        console.log(data.property_type)
        console.log(data.rooms_number)
      },
      error: function (error_data) {
        console.log(error_data)
      },
    }),
  })

  if (selectedChart) {
    selectedChart.destroy()
  }
  if (selectedBar) {
    selectedBar.destroy()
  }

  load_graph_data()
  load_bar_data()
}

function getTimePeriod() {
  let selectedTimePeriod = document.getElementById('time_period_form').value
  let url = new URL(window.location.href)
  url.searchParams.set('time_period', selectedTimePeriod)
  history.pushState({}, '', url.href)

  let selectedMasterProject = url.searchParams.get('master_project')
  let selectedProjectName = url.searchParams.get('project_name')
  let selectedBuildingName = url.searchParams.get('building_name')
  let selectedPropertyType = url.searchParams.get('property_type')
  let selectedRoomsNumber = url.searchParams.get('rooms_number')
  // let selectedTimePeriod = url.searchParams.get('time_period')

  $.ajax({
    method: 'GET',
    url: 'https://www.dxbstates.com/latest_transactions',
    data: {
      master_project: selectedMasterProject,
      project_name: selectedProjectName,
      building_name: selectedBuildingName,
      property_type: selectedPropertyType,
      rooms_number: selectedRoomsNumber,
      time_period: selectedTimePeriod,
    },
    xhrFields: {
      withCredentials: true,
    },
    async: false,
    cache: false,
    success: $.ajax({
      method: 'GET',
      data: {
        master_project: selectedMasterProject,
        project_name: selectedProjectName,
        building_name: selectedBuildingName,
        property_type: selectedPropertyType,
        rooms_number: selectedRoomsNumber,
        time_period: selectedTimePeriod,
      },
      url: "{% url 'ajax_url' %}",
      xhrFields: {
        withCredentials: true,
      },
      success: function (data) {
        console.log(data.master_project)
        console.log(data.project_name)
        console.log(data.building_name)
        console.log(data.property_type)
        console.log(data.rooms_number)
        console.log(data.time_period)
      },
      error: function (error_data) {
        console.log(error_data)
      },
    }),
  })

  if (selectedChart) {
    selectedChart.destroy()
  }
  if (selectedBar) {
    selectedBar.destroy()
  }

  load_graph_data()
  load_bar_data()
}
