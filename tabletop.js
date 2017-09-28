
            function initTabletop() {
                console.log('tabletop')
            
                var public_spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1XVO1smiI3iOoLJt1nPkmnxqWb2Zi4okiDTtghdBfUcQ/pubhtml';    
                // get orderby and reverse queries for table ordering
                var orderby = getQueryVariable('orderby');
                if (! orderby) {
                    orderby = 'Name';
                }

                var reverse = getQueryVariable('reverse');
                if (! reverse) {
                    reverse = false;
                } else {
                    reverse = true;
                }


                var loc = window.location.pathname;
                var dir = loc.substring(0, loc.lastIndexOf('/'));

                // query the spreadsheet, and call showInfo() on callback
                
                Tabletop.init( { key: public_spreadsheet_url,
                                 callback: showInfo,
                                 simpleSheet: true,
                                 orderby: orderby,
                                 reverse: reverse ,
                                 proxy: dir,
                                 } );
               
                
                //var data = JSON.parse(rawdata);
                //showInfo(data);
                          }
                          