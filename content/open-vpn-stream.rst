OpenVPN on Beaglebone Black
###########################

:date: 2017-06-12 19:51
:category: random
:slug: openvpn-on-beaglebone-black
:authors: Ben Hoff
:summary: Getting OpenVPN working on beaglebone black
:status: draft


All right, let's install OpenVPN_ on a `beaglebone black <https://beagleboard.org/black>`_.

First I need to flash the thing.

So downloading_ the latest image from the repository, I need to unpack the image.

.. code-block:: console

    $ unxz bone-debian-X.X-iot-armhf-YYYY-MM-DD-4gb.img.xz

Ok, now I've got the uncompressed image.

.. code-block:: console

    $ lsblk
    
Shows the SD card I've just plugged in as /dev/sdc

.. code-block:: console

    sudo mount /dev/sdc /mnt

Then let's write our image.

.. code-block:: console

    sudo dd if=bone-debian*.img of=/dev/sdc bs=512 status=progress

Believe me, that little 'status=progress' bit is a life saver. Otherwise you have no idea how long it's going to take. I also don't know how to kill dd without pulling out the drive.

The last two sentences are related.

I'm following this_ blog post by the way. 
Since you're going to be awhile. 
My image size was 4 gigabytes with a transfer speed of ~6 megabytes/second.

And it died. 13 minutes of waiting... Ok. Let's try again. (Iotop_ will show you if the copy is still working)

Died again. 3rd times the charm.
Nope. Ok on to something else. Normally I'd just go get a new SD card, but I'm transferring this through like 3 adapters and it's been known to give me issues in the past.

Stack Exchange to the rescue. According to `this post`_ I should just be able to resume where I left off.

.. _`this post`: https://unix.stackexchange.com/questions/180330/resuming-a-dd-of-an-entire-disk

OK, so my write this time failed at XXXX bytes.

.. code-block:: console

    sudo dd if=bone-debian*.img of=/dev/sdc status=progress

I'm a goddamn Linux wizard. Well, frostschutz_ is at least. I bet he even knows how to read the dd man pages!

Actually looks like my dd just didn't terminate correctly.

You'll want to seek and skip. The output of should look something like this.

.. code-block:: console

    6963200+0 records in
    6963200+0 records out
    3565158400 bytes (3.6 GB, 3.3 GiB) copied, 732.023 s, 4.9 MB/s

you'll want to use the records as the type.

Holding down the boot button and we're in business.

.. code-block:: console

    $ ssh debian@192.168.7.2

The password was in the banner for me.


.. code-block:: console

    $ sudo su
    $ apt-get update
    $ apt-get install openvpn easy-rsa

I know things are going well when I forget to type a log. I'm following these_ instructions. It's pretty simple.

.. _these: https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-16-04


http://kacangbawang.com/beagleboneblack-revc-debloat-part-1/

.. _frostschutz: https://unix.stackexchange.com/users/30851/frostschutz

.. _downloading: https://beagleboard.org/latest-images
.. _OpenVPN: https://openvpn.net/
.. _this: http://derekmolloy.ie/write-a-new-image-to-the-beaglebone-black/
.. _Iotop: http://guichaz.free.fr/iotop/
