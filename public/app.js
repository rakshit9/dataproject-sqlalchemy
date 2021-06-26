function featchdata() {
    
    fetch('data.json')
    .then(response => response.json())
    .then(loadData);
}
featchdata();

function loadData(data)
{   
    authcapital(data.authoried_cap);
    registercompany(data.company_register);
    numberofcompany(data.number_of_company);
    stackresult(data.stack_result);
    
}
function authcapital(auth_data){    
    store_array = [];
    for(let item in auth_data){
        store_array.push([item,auth_data[item]])
    }   
    Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Authorized Capital in Maharashtra',
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        subtitle: {
            text: 'Source: <a href="https://data.gov.in/resources/company-master-data-maharashtra-upto-21st-april-2018">data.gov</a>',
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        xAxis: {
            type: 'category',
            labels: {                
                style: {
                    fontSize: '10px',
                    fontFamily: 'Verdana, sans-serif',
                    color: '#000'
                }
            },
            min: 0,
            title: {
                text: 'Capitals',
                style: {                    
                    color: '#0068a5'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number of companies',
                style: {                    
                    color: '#0068a5'
                }
            }
            
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Population in 2017: <b>{point.y:.1f} millions</b>'
        },
        series: [{
            name: 'Population',
            data: store_array,
            dataLabels: {
                enabled: true,
                rotation: 0,
                color: '#FFFFFF',
                align: 'center',
                format: '{point.y:.f}',
                y: 20,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif',
                    
                }
            }
        }]
    });
                  
}




function registercompany(company_register){
    store_array = [];
    
    for(let item in company_register){
        store_array.push([String(parseInt(item)),company_register[item]])
    }
    Highcharts.chart('company_register', {
        chart: {
            type: 'column'
        },
        title: {
            text: "Company Registration in Maharashtra From 2009 to 2018",
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        subtitle: {
            text: 'Source: <a href="https://data.gov.in/resources/company-master-data-maharashtra-upto-21st-april-2018">data.gov</a>',
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        xAxis: {
            type: 'category',
            labels: {            
                style: {
                    fontSize: '10px',
                    fontFamily: 'Verdana, sans-serif',
                    color: '#000'
                }
            },
            min: 0,
            title: {
                text: 'Date of Registration',
                style: {                    
                    color: '#0068a5'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number of Companies',
                style: {                    
                    color: '#0068a5'
                }
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Population in 2017: <b>{point.y:.1f} millions</b>'
        },
        series: [{
            name: 'Population',
            data: store_array,
            dataLabels: {
                enabled: true,
                rotation: 0,
                color: '#FFFFFF',
                align: 'center',
                format: '{point.y:.f}',
                y: 20,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Lucida Console, Courier, monospace'
                    

                }
            }
        }]
    });
                  

}


function numberofcompany(number_of_company){    
    store_array = [];
    for(let item in number_of_company){
        store_array.push([item,number_of_company[item]])
    }    
    Highcharts.chart('number_of_company', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Principal Business Activity in 2015',
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        subtitle: {
            text: 'Source: <a href="https://data.gov.in/resources/company-master-data-maharashtra-upto-21st-april-2018">data.gov</a>',
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        xAxis: {
            type: 'category',
            labels: {                
                style: {
                    fontSize: '10px',
                    fontFamily: 'Verdana, sans-serif',
                    color: "#000",
                }
            },
            title: {
                text: 'Business Activity Name',
                style: {                    
                    color: '#0068a5'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number of companies',
                style: {                    
                    color: '#0068a5'
                }
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Population in 2017: <b>{point.y:.1f} millions</b>'
        },
        series: [{
            name: 'Population',
            data: store_array,
            dataLabels: {
                enabled: true,
                rotation: 0,
                color: '#FFFFFF',
                align: 'center',
                format: '{point.y:.f}',
                y: 20,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
                  

}


function stackresult(stack_result){   
    obj_name = Object.keys(stack_result);
    obj_value =Object.values(stack_result);

    Highcharts.chart('stack_result', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Principal Business Activities in Maharashtra from 2001 to 2010',
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        subtitle: {
            text: 'Source: <a href="https://data.gov.in/resources/company-master-data-maharashtra-upto-21st-april-2018">data.gov</a>',
            style: {                
                fontFamily: 'Lucida Console, Courier, monospace',
                color: '#0068a5'
            }
        },
        xAxis: {
            categories: obj_value[0],
            crosshair: true,
            labels: {
                style: {
                    fontSize: '10px',
                    fontFamily: 'Verdana, sans-serif',
                    color: "#000",
                }
            },
            title: {
                text: 'Number Of Companies',
                style: {                    
                    color: '#0068a5'
                }
            }
            
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Total Companies',
                style: {                    
                    color: '#0068a5'
                }
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [
           {
               name:obj_name[1],
               data: obj_value[1]

           },
            {
                name: obj_name[2],
                data:obj_value[2]
        
            },
            {
                name: obj_name[3],
                data:obj_value[3]
        
            },
            {
                name: obj_name[4],
                data: obj_value[4]
        
            },
            {
                name: obj_name[5],
                data: obj_value[5]
        
            },

        ]
    });
                  
    
                  

}



