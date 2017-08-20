Shit to make:
						put an x once its done
the class and subclasses				[ ]

		class item
			itemName		//the item obviously
			itemCategory		//manually entered based upon category and page it comes from
			buyLimit		//manually entered into database once, constant
			buyPrice		//pulled from forums every 10 minutes
			sellPrice		//same as above
			percentChange		//calculated from previous, first derivate with respect to time
			timeSinceLastChange	//the time the item was last changed
			avgTimeToUpdate 	//how often this item usually updates (in seconds)
			percentConfidence	//need a logorathmic equation based on time since update vs time it usually takes to change, percent change, buy limit, similiar items changes

			subclass itemCategory //not actually gonna be called itemCatagory, its gonna actually be the category
				itemCategory			// same shit but for a bunch of items at once, so we'd need a few of these subclasses
				itemNameList<String>		// all the items that its pooling from
				buyPriceList<String>
				sellPriceList<String>
				percentChangeList<String>	//calculated from previous, first derivate with respect to time
				timeSinceLastChange<String>
				avgTimeToUpdateList<String>	//how often this item usually updates (in seconds)
				percentConfidenceList<String>	//need a logorathmic equation based on time since update vs time it usually takes to change, percent change, similiar items changes




main							[ ]
	//runs a bunch of methods
	1) query forums to find most recent version of the page 	// it will be the page QID number in the format XX-XX-XXX-XXXXXXXX
	2) go to the page for the QID					// the QID goes in a set spot in the URL
	3a) if the database is empty, populate it			// run through every page of the thread and record buy and sell prices and the times they are updated
	3b) else populate entries since most recent database entry
	4) run calculations


populateItemFromCategory(itemCategory)			[ ]	
	// populates the database with the stuff itemCategory collects

	return null

lookup(itemCatgory)					[ ]
	// query forums based on category (so which page its looking for)
	
	return QID

examineThread(QID)					[ ]
	// opens proper URL using QID
	// checks if the database is empty, populates it as per specifications in main
	// update the database with all the values aquired (buyPrice, sellPrice,  timeSinceLastChange)
	// since sometimes the category posts are edited, always add the most recent one to the database and only update time if the values change

	return null

calculateChange(itemName)				[ ]
	// calculates percent change for the item and updates database

	return null

calculateAvgTimeToUpdate(itemName)			[ ]
	// should discard fastest and slowest 10% of updates
	// calculates the average time it takes the item to update based on the remaining data
	// updateDataBase(itemName, AvgTimeToUpdate, placeHolderToTellItWhatThisValueIs)

	return null

percentConfidence(itemName)				[ ]
	// calculates the confidence level based on perviously described values
	// this algorithm will require some fine tuning

	return null

database display					[ ]
	suggestions based on profitabilty from confidence
		a category for low buy limit items, <= 10
		a category for high buy limit items, > 10
		should display item name, change in value, percent change in value, sell - buy prices, confidence level
	Overall page listing all items sorted by category
		displays item name, buy limit, sell - buy price, sell price, buy price, change, confidence

scrape(webpage)						[ ]


potential modules:
	pandas - data analysis
	scrapy - scraping
	scrapyd - spider stuff
	Django - web app
	